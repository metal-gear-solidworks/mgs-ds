from pygame import joystick
import threading

class ControllerError(Exception):
    pass

class JoystickState:
    def failsafe(self):
        self.state = {
            'analog' : [
                0,
                0,
                0,
                0,
                0,
                0
            ],

            'dpad' : [
                0,
                0
            ],

            'buttons' : [
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False
            ]
        }

    def update_state(self, gamepad):
        if not isinstance(gamepad, joystick.Joystick):
            raise TypeError("'gamepad' argument must be a Joystick object")

        try:
            conditions = [
                gamepad.get_numaxes() == 6,
                gamepad.get_numbuttons() == 10,
                gamepad.get_numhats() == 1
            ]
        except:
            self.failsafe()
            raise

        if not all(conditions):
            raise ControllerError('gamepad does not appear to be an Xbox controller')

        try:
            threading.Lock.acquire()
            for index, axis in enumerate(self.state.analog):
                axis = gamepad.get_axis(index)
            
            self.state.dpad = gamepad.get_hat(0)

            for index, button in enumerate(self.state.buttons):
                button = gamepad.get_button()
        except:
            self.failsafe()
            raise
        finally:
            threading.Lock.release()

    def __init__(self):
        joystick.init()
        self.failsafe()

def read_controller():
    pass

if __name__ == '__main__':
    gamepad = JoystickState()

    threading.Thread(target=read_controller).start()
