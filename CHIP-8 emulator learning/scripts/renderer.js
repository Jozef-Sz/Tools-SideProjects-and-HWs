export default class Renderer {
    constructor(scale) {
        this.scale = scale;

        // Chip-8 display size is 64x32 pixels
        this.cols = 64;
        this.rows = 32;

        this.canvas = document.querySelector('canvas');
        this.ctx = this.canvas.getContext('2d');

        
        this.canvas.width = this.cols * this.scale;
        this.canvas.height = this.rows * this.scale;

        this.display = new Array(this.cols * this.rows);
    }

    /**
     * @description set the given pixel to it's opposite value and return new state
     * @param {number} x x-coordinate of the canvas
     * @param {number} y y-coordinate fo the canvas
     * @returns {boolean} true if the pixel was ereased and false if it was set
     */
    setPixel(x, y) {
        // If a pixel is positioned outside of the bounds of 
        // the display, it should wrap around to the opposite side
        if (x > this.cols) {
            x -= this.cols;
        } 
        else if (x < 0) {
            x += this.cols;
        }

        if (y > this.rows) {
            y -= this.rows;
        }
        else if (y < 0) {
            y += this.rows;
        }

        // Is a 1d array index from a 2d grid
        const pixelIndex = x + y * this.cols;

        // This below is a bitwise XOR operation, just look at the truth table
        // and you'll get it. This basicaly is a flip-flop 0 flips to 1 and 1 to 0
        this.display[pixelIndex] ^= 1;

        return !this.display[pixelIndex];
    }

    /**
     * @description render display array (buffer) to the screen
     */
    render() {
        // Clears the screen every render cycle
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        // Set background color to black (more authentic)
        this.ctx.fillStyle = "#000";
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);


        for (let i = 0; i < this.cols * this.rows; i++) {

            // Converting 1d indexes to 2d coordinates
            const x = (i % this.cols) * this.scale;
            const y = Math.floor(i / this.cols) * this.scale;

            // If pixel is 1 then set it to white color and place it
            if (this.display[i]) {
                this.ctx.fillStyle = '#FFF';

                this.ctx.fillRect(x, y, this.scale, this.scale);
            }
        }
    }

    /**
     * @description this function completely clears the display array by reinitializing it
     */
    clear() {
        this.display = new Array(this.cols * this.rows);
    }
}