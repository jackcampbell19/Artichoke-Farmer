import random

from interfaces import MotorController
from sys import argv


# 5000, 4810, 4200

# tool pos 1) x,y: 390,35   z-grab: 2100


def run(x, y, z):
    mx = 2 ** 16 - 1
    if x > mx or y > mx or z > mx:
        print("Value exceeded max")
        return
    data = [
        0b00010001,
        x >> 8,
        (x & 255),
        y >> 8,
        (y & 255),
        z >> 8,
        (z & 255),
    ]
    print(motor_controller.send_command(data))

def arc_move(cx, cy, cz, rx, ry, rz, deg):
    motor_controller.send_command([
        0b01110001,
        cx >> 8,
        cx & 255,
        cy >> 8,
        cy & 255,
        cz >> 8,
        cz & 255,
        rx >> 8,
        rx & 255,
        ry >> 8,
        ry & 255,
        rz >> 8,
        rz & 255,
        deg >> 8,
        deg & 255
    ])


def exchange_tool(t):
    motor_controller.send_command([0b0010 << 4 | (t & 0b1111)])


if __name__ == '__main__':
    motor_controller = MotorController(busy_line=14)
    # motor_controller.send_command([0b01100000])  # Measure
    motor_controller.send_command([0b01000000])  # Dispense paint
    # arc_move(5000, 5000, 0, 0, 2000, 0, 180)
    # motor_controller.send_command([0])  $ Home
    # for _ in range(10):
    #     run(random.randint(400, 500), random.randint(400, 500), 0)
    # exchange_tool(1)
