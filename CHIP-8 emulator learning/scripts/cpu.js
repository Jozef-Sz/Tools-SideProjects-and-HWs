export default class CPU {
    constructor(renderer, keyboard, speaker) {
        this.renderer = renderer;
        this.keyboard = keyboard;
        this.speaker = speaker;

        // 4kB of memory 
        this.memory = new Uint8Array(4096);

        // 16 8-bit registers
        this.v = new Uint8Array(16);

        // Stores memory addresses
        this.i = 0;

        this.delayTimer = 0;
        this.soundTimer = 0;

        // Program counter, stores the currently executing address
        this.pc = 0x200;

       this.stack = new Array();

       this.paused = false;
       this.speed = 10;
    }

    loadSpritesIntoMemory() {
        // Array of hex values for each sprite. Each sprite is 5 bytes.
        // The technical reference provides us with each one of these values.
        const sprites = [
            0xF0, 0x90, 0x90, 0x90, 0xF0, // 0
            0x20, 0x60, 0x20, 0x20, 0x70, // 1
            0xF0, 0x10, 0xF0, 0x80, 0xF0, // 2
            0xF0, 0x10, 0xF0, 0x10, 0xF0, // 3
            0x90, 0x90, 0xF0, 0x10, 0x10, // 4
            0xF0, 0x80, 0xF0, 0x10, 0xF0, // 5
            0xF0, 0x80, 0xF0, 0x90, 0xF0, // 6
            0xF0, 0x10, 0x20, 0x40, 0x40, // 7
            0xF0, 0x90, 0xF0, 0x90, 0xF0, // 8
            0xF0, 0x90, 0xF0, 0x10, 0xF0, // 9
            0xF0, 0x90, 0xF0, 0x90, 0x90, // A
            0xE0, 0x90, 0xE0, 0x90, 0xE0, // B
            0xF0, 0x80, 0x80, 0x80, 0xF0, // C
            0xE0, 0x90, 0x90, 0x90, 0xE0, // D
            0xF0, 0x80, 0xF0, 0x80, 0xF0, // E
            0xF0, 0x80, 0xF0, 0x80, 0x80  // F
        ];

        // According to the technical reference, sprites are stored in the interpreter 
        // section of memory starting at hex 0x000
        for (let i = 0; i < sprites.length; i++) {
            this.memory[i] = sprites[i];
        }
    }

    /**
     * @description loading the given program file into the memory
     * @param {Uint8Array} program program file
     */
    loadProgramIntoMemory(program) {
        const programStartIndex = 0x200;
        let newProgramIndex;
        for (let loc = 0; loc < program.length; loc++) {
            newProgramIndex = programStartIndex + loc;
            this.memory[newProgramIndex] = program[loc];
        }
    }

    /**
     * @description loading the given rom from the roms folder with XMLHttpRequest and loadProgramIntoMemory
     * @param {string} romName name of the rom we want to load
     */
    loadRom(romName) {
        const request = new XMLHttpRequest();
        const self = this;

        request.onload = function() {
            if (request.response) {
                const program = new Uint8Array(request.response);
                self.loadProgramIntoMemory(program);
            }
        }

        request.open('GET', 'roms/' + romName);
        request.responseType = 'arraybuffer';
        request.send();
    }

    /**
     * @description represents one cycle of the cpu, here the cpu is fetching opcodes, executes 
     *              instructions, handles timers, sound and rendering
     */
    cycle() {
        for (let i = 0; i < this.speed; i++) {
            if (!this.paused) {
                const opcode = (this.memory[this.pc] << 8 | this.memory[this.pc + 1]);
                this.executeInstruction(opcode);
            }
        }

        if (!this.paused) {
            this.updateTimers();
        }

        this.playSound();
        this.renderer.render();
    }

    executeInstruction(opcode) {
        // Increment the program counter to prepare it for the next instruction.
        // Each instruction is 2 bytes long, so increment it by 2.
        this.pc += 2;

        // x - A 4-bit value, the lower 4 bits of the high byte of the instruction
        // So for example from 0x5460, it would be 0x4
        const x = (opcode & 0x0F00) >> 8;

        // y - A 4-bit value, the upper 4 bits of the low byte of the instruction
        // So for example form 0x5460, it would be 0x6
        const y = (opcode & 0x00F0) >> 4;

        switch (opcode & 0xF000) {
            case 0x000:
                switch (opcode) {
                    case 0x00E0:
                        // CLS
                        this.renderer.clear();
                        break;
                    case 0x00EE:
                        // RET
                        this.pc = this.stack.pop();
                        break;
                }

                break;
            case 0x1000:
                // JP
                this.pc = (opcode & 0xFFF);
                break;
            case 0x2000:
                // CALL
                this.stack.push(this.pc);
                this.pc = (opcode & 0xFFF);
                break;
            case 0x3000:
                // SE Vx, byte
                if (this.v[x] === (opcode & 0xFF)) {
                    this.pc += 2;
                }
                break;
            case 0x4000:
                // SNE Vx, byte
                if (this.v[x] !== (opcode & 0xFF)) {
                    this.pc += 2;
                }
                break;
            case 0x5000:
                // SE Vx, Vy
                if (this.v[x] === this.v[y]) {
                    this.pc += 2;
                }
                break;
            case 0x6000:
                // LD Vx, byte
                this.v[x] = (opcode & 0xFF);
                break;
            case 0x7000:
                // ADD Vx, byte
                this.v[x] += (opcode & 0xFF);
                break;
            case 0x8000:
                switch (opcode & 0xF) {
                    case 0x0:
                        // LD Vx, Vy
                        this.v[x] = this.v[y];
                        break;
                    case 0x1:
                        // OR Vx, Vy
                        this.v[x] |= this.v[y];
                        break;
                    case 0x2:
                        // AND Vx, Vy
                        this.v[x] &= this.v[y];
                        break;
                    case 0x3:
                        // XOR Vx, Vy
                        this.v[x] ^= this.v[y];
                        break;
                    case 0x4:
                        // ADD Vx, Vy
                        // If the result is greater than 8 bits VF is set to 1, otherwise 0. 
                        // Only the lowest 8 bits of the result are kept, and stored in Vx.
                        const sum = (this.v[x] += this.v[y]);
                        
                        this.v[0xF] = 0;

                        if (sum > 0xFFF) {
                            this.v[0xF] = 1;
                        }

                        this.v[x] = sum;
                        break;
                    case 0x5:
                        // SUB Vx, Vy
                        this.v[0xF] = 0;

                        if (this.v[x] > this.v[y]) {
                            this.v[0xF] = 1;
                        }

                        this.v[x] -= this.v[y];
                        break;
                    case 0x6:
                        // SHR Vx {, Vy}
                        this.v[0xF] = (this.v[x] & 0x1);

                        this.v[x] >>= 1;
                        break;
                    case 0x7:
                        // SUBN Vx, Vy
                        this.v[0xF] = 0;

                        if (this.v[y] > this.v[x]) {
                            this.v[0xF] = 1;
                        }

                        this.v[x] = this.v[y] - this.v[x];
                        break;
                    case 0xE:
                        // SHL Vx {, Vy}
                        this.v[0xF] = (this.v[x] & 0x80);
                        this.v[x] <<= 1;
                        break;
                }
        
                break;
            case 0x9000:
                // SNE Vx, Vy
                if (this.v[x] !== this.v[y]) {
                    this.pc += 2;
                }
                break;
            case 0xA000:
                // LD I, addr
                this.i = (opcode & 0xFFF);
                break;
            case 0xB000:
                // JP V0, addr
                this.pc = (opcode & 0xFFF) + this.v[0];
                break;
            case 0xC000:
                // RND Vx, byte  (random number)
                const rand = Math.floor(Math.random() * 0xFF);

                this.v[x] = rand & (opcode & 0xFF);
                break;
            case 0xD000:
                const width = 8;
                const height = (opcode & 0xF);

                this.v[0xF] = 0;

                for (let row = 0; row < height; row++) {
                    let sprite = this.memory[this.i + row];

                    for (let col = 0; col < width; col++) {
                        // If the bit (sprite) is not 0, render/erase the pixel
                        if ((sprite & 0x80) > 0) {
                            // If setPixel returns 1, which means a pixel was erased, set VF to 1
                            if (this.renderer.setPixel(this.v[x] + col, this.v[y] + row)) {
                                this.v[0xF] = 1;
                            }
                        }

                        // Shift the sprite left 1. This will move the next next col/bit of the sprite into the first position.
                        // Ex. 10010000 << 1 will become 0010000
                        sprite <<= 1;
                    }
                }
                break;
            case 0xE000:
                switch (opcode & 0xFF) {
                    case 0x9E:
                        // SKP Vx
                        if (this.keyboard.isKeyPressed(this.v[x])) {
                            this.pc += 2;
                        }
                        break;
                    case 0xA1:
                        // SKNP Vx
                        if (!this.keyboard.isKeyPressed(this.v[x])) {
                            this.pc += 2;
                        }
                        break;
                }
        
                break;
            case 0xF000:
                switch (opcode & 0xFF) {
                    case 0x07:
                        // LD Vx, DT
                        this.v[x] =this.delayTimer;
                        break;
                    case 0x0A:
                        // LD Vx, K
                        this.paused = true;

                        this.keyboard.onNextKeyPress = function(key) {
                            this.v[x] = key;
                            this.paused = false;
                        }.bind(this);
                        break;
                    case 0x15:
                        // LD DT, Vx
                        this.delayTimer = this.v[x];
                        break;
                    case 0x18:
                        // LD ST, Vx
                        this.soundTimer = this.v[x];
                        break;
                    case 0x1E:
                        // ADD I, Vx
                        this.i += this.v[x];
                        break;
                    case 0x29:
                        // LD F, Vx - ADD I, Vx
                        this.i = this.v[x] * 5;
                        break;
                    case 0x33:
                        // LD B, Vx
                        // Get the hundreds digit and place it in I.
                        this.memory[this.i] = parseInt(this.v[x] / 100);

                        // Get tens digit and place it in I+1. Gets a value between 0 and 99,
                        // then divides by 10 to give us a value between 0 and 9.
                        this.memory[this.i + 1] = parseInt((this.v[x] % 100) / 10);

                        // Get the value of the ones (last) digit and place it in I+2.
                        this.memory[this.i + 2] = parseInt(this.v[x] % 10);
                        break;
                    case 0x55:
                        // LD [I], Vx
                        for (let registerIndex = 0; registerIndex <= x; registerIndex++) {
                            this.memory[this.i + registerIndex] = this.v[registerIndex];
                        }
                        break;
                    case 0x65:
                        // LD Vx, [I]
                        for (let registerIndex = 0; registerIndex <= x; registerIndex++) {
                            this.v[registerIndex] = this.memory[this.i + registerIndex];
                        }
                        break;
                }
        
                break;
        
            default:
                throw new Error('Unknown opcode ' + opcode);
        }
    }

    /**
     * @description updatind timers acording to CHIP-8's tech. reference
     */
    updateTimers() {
        if (this.delayTimer > 0) {
            this.delayTimer -= 1;
        }

        if (this.soundTimer > 0) {
            this.soundTimer -= 1;
        }
    }

    /**
     * @description playing sound, sound when the sound timer is non-zero (actualy, greater than zero)
     */
    playSound() {
        if (this.soundTimer > 0) {
            this.speaker.play(440);
        }
        else {
            this.speaker.stop();
        }
    }
}