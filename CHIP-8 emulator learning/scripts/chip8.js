import Renderer from './renderer.js';

const renderer = new Renderer(5);

const fps = 60;
let loop, fpsInterval, startTime, now, then, elapsed;


function init() {
    fpsInterval = 1000 / fps;
    then = Date.now();
    startTime = then;

    loop = requestAnimationFrame(step);
}

function step() {
    now = Date.now();
    elapsed = now - then;

    if (elapsed > fpsInterval) {
        // Cycle the CPU. We'll come back to this later and fill it out.
    }

    loop = requestAnimationFrame(step);
}

init();