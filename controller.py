from pygame import joystick

NUM_AXES = 6
NUM_BUTTONS = 11
NUM_HATS = 1

class GamepadState:
    def __init__(self) -> None:
        self.axes = [0] * NUM_AXES
        self.buttons = [False] * NUM_BUTTONS
        self.hat_x = 0
        self.hat_y = 0
    
    def update_state(self, input: joystick.Joystick) -> None:
        conditions = [
            input.get_numaxes() == NUM_AXES,
            input.get_numbuttons() == NUM_BUTTONS,
            input.get_numhates() == NUM_HATS
        ]

        if all(conditions):
            self.axes = input.get_axis(i) for i in range(NUM_AXES)
            self.buttons = input.get_button(i) for i in range(NUM_BUTTONS)
            hat = input.get_hat(0)
            self.hat_x = hat[0]
            self.hat_y = hat[1]
        else:
            __init__()

    def pack(self) -> bytes:
        # temporary hardcoded value
        return bytes([
            0xFF,
            0x00,
            0x00,
            0x21,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x21,
            0xF0
        ])

class Controller:
    def __init__(self) -> None:
        self.gamepad = GamepadState()