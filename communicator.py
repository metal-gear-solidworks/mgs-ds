import serial

class Communicator:
    def __init__(self, port: str) -> None:
        try:
            self.port = serial.Serial(port)
        except:
            print('Error opening serial port')