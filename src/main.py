import random

from interfaces import MotorController

HOME_CODE = 0
MOVE_CODE = 1
CUP_HOLDER_CODE = 3
CONFIGURE_CODE = 5


def get_command(b: int):
    return b >> 4


if __name__ == '__main__':
    motor_controller = MotorController(busy_line=14)
    file_path = '/home/pi/software/test.art'
    with open(file_path, 'rb') as file:
        instruction = []
        while True:
            byte = file.read(1)
            if not byte:
                break
            b = ord(byte)
            instruction.append(b)
            if get_command(b) == MOVE_CODE:
                for _ in range(6):
                    instruction.append(ord(file.read(1)))
            if get_command(b) == CONFIGURE_CODE:
                for _ in range(25):
                    instruction.append(ord(file.read(1)))
            motor_controller.send_command(instruction)
            instruction = []

