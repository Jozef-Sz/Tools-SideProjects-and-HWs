export default class CPU {
    constructor(renderer, keyboard, speaker) {
        this.renderer = renderer;
        this.keyboard = keyboard;
        this.speaker = speaker;

        // 4kB of memory 
        this.memory = new Uint8Array(4096);
    }
}