// Return true if gamepad support exists on this browser

function supportsGamepads() {
    return !!(navigator.getGamepads);
}


let gamepads = navigator.getGamepads();

for (let i = 0; i < gamepads.length; i++) {
    console.log("Gamepad " + i + ":");

    if (gamepads[i] === null) {
        console.log("[null]");
        continue;
    }

    if (!gamepads[i].connected) {
        console.log("[disconnected]");
        continue;
    }

    console.log("    Index: " + gamepads[i].index);
    console.log("    ID: " + gamepads[i].id);
    console.log("    Axes: " + gamepads[i].axes.length);
    console.log("    Buttons: " + gamepads[i].buttons.length);
    console.log("    Mapping: " + gamepads[i].mapping);
}
