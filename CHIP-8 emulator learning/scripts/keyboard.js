export default class Keyboard {
    constructor(debug=false) {
        this.debug = debug;
        this.KEYMAP = {
            '1': 0x1,
            '2': 0x2,
            '3': 0x3,
            '4': 0xc,
            'q': 0x4, 
            'w': 0x5, 
            'e': 0x6,
            'r': 0xD,
            'a': 0x7,
            's': 0x8,
            'd': 0x9,
            'f': 0xE,
            'z': 0xA,
            'x': 0x0,
            'c': 0xB,
            'v': 0xF 

        };

        this.keysPressed = {};

        // Some Chip-8 instructions require waiting for the next keypress
        this.onNextKeyPress = null;

        window.addEventListener('keydown', this.onKeyDown.bind(this), false);
        window.addEventListener('keyup', this.onKeyUp.bind(this), false);
    }

    isKeyPressed(key) {
        return this.keysPressed[key];
    }

    onKeyDown(event) {
        const key = this.KEYMAP[event.key];
        this.keysPressed[key] = true;

        // Make sure onNextKeyPress is initialized and the pressed key is actually mapped to a Chip-8 key
        if (this.onNextKeyPress !== null && key) {
            this.onNextKeyPress(key);
            this.onNextKeyPress = null;
        }

        if (this.debug) {
            console.log(this.keysPressed);
        }
    }

    onKeyUp(event) {
        const key = this.KEYMAP[event.key];
        delete this.keysPressed[key];

        if (this.debug) {
            console.log(this.keysPressed);
        }
    }
}