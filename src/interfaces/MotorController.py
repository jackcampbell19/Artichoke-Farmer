from typing import Sequence, List
from MakerToolbox import RPi3, InputPin

import smbus2
import time


class MotorController:

    def __init__(self, busy_line: int, address: int = 8):
        self._busy_line: InputPin = RPi3.input_pin(busy_line)
        self._bus = smbus2.SMBus(1)
        self._address: int = address
        self._buffer_size: int = 16
        self._controller_error_code: int = 0b00000000
        self._controller_null_code: int = 0b11111111

    def flush_buffer(self):
        pass

    def send_command(self, command: List[int]) -> bool:
        for byte in command:
            try:
                self._bus.write_byte(self._address, byte)
            except TimeoutError or IOError as e:
                print(f"Send failed: {e}")
                self.flush_buffer()
                return False
        start = time.time()
        while not self._busy_line.read():
            if time.time() - start > 0.05:
                print('Busy line was not detected')
                return False
        while self._busy_line.read():
            pass
        try:
            self._bus.write_byte(self._address, 0)
            response = self._bus.read_i2c_block_data(self._address, 0, 2)
            code = response[0] << 8 | response[1]
            print(code)
            return code != self._controller_error_code
        except TimeoutError or OSError as e:
            print(f"Failed to get response code from controller: {e}")
            self.flush_buffer()
            return False
