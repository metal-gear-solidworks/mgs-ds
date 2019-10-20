from pygame import joystick
from enum import Enum
from time import sleep
import threading

class ControllerError(Exception):
    pass

class ConnectionState(Enum):
    DISCONNECTED = 0
    CONNECTED = 1

class JoystickState:
    def _failsafe(self):
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

    def _update_state(self):
        try:
            conditions = [
                self._gamepad.get_numaxes() == 6,
                self._gamepad.get_numbuttons() == 10,
                self._gamepad.get_numhats() == 1
            ]
        except:
            self._failsafe()
            raise

        if not all(conditions):
            self._failsafe()
            raise ControllerError('gamepad does not appear to be an Xbox controller')

        try:
            for index, axis in enumerate(self.state.analog):
                axis = self._gamepad.get_axis(index)
            
            self.state.dpad = self._gamepad.get_hat(0)

            for index, button in enumerate(self.state.buttons):
                button = self._gamepad.get_button()
        except:
            self._failsafe()
            raise

    def _disconnected(self):
        self._failsafe()
    
    def _connected(self):
        with self._lock:
            try:
                self._update_state()
            except:
                pass

    def _check_connection(self):
        with self._lock:
            self.connection = ConnectionState.CONNECTED
            try:
                self._gamepad = joystick.Joystick(0)
            except:
                self.connection = ConnectionState.DISCONNECTED
    
    def run(self):
        if self.connection:
            self._connected()
        else:
            self._disconnected()
        
        self._check_connection()

    def __init__(self):
        joystick.init()
        self._lock = threading.Lock()
        self._check_connection()
        self._failsafe()

def read_controller(controller):
    while True:
        controller.run()
        sleep(0.05)

def broadcast_controller(controller):
    while True:
        print(controller.state)
        sleep(0.05)

if __name__ == '__main__':
    controller = JoystickState()

    threading.Thread(target=read_controller, args=[controller]).start()
    threading.Thread(target=broadcast_controller, args=[controller]).start()