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
                        break;
                    case 0x3:
                        break;
                    case 0x4:
                        break;
                    case 0x5:
                        break;
                    case 0x6:
                        break;
                    case 0x7:
                        break;
                    case 0xE:
                        break;
                }
        
                break;
            case 0x9000:
                break;
            case 0xA000:
                break;
            case 0xB000:
                break;
            case 0xC000:
                break;
            case 0xD000:
                break;
            case 0xE000:
                switch (opcode & 0xFF) {
                    case 0x9E:
                        break;
                    case 0xA1:
                        break;
                }
        
                break;
            case 0xF000:
                switch (opcode & 0xFF) {
                    case 0x07:
                        break;
                    case 0x0A:
                        break;
                    case 0x15:
                        break;
                    case 0x18:
                        break;
                    case 0x1E:
                        break;
                    case 0x29:
                        break;
                    case 0x33:
                        break;
                    case 0x55:
                        break;
                    case 0x65:
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