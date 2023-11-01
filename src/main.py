from interfaces import MotorController
from sys import argv


# 5000, 4810, 4200

# tool pos 1) x,y: 390,35   z-grab: 2100


def run(x, y, z):
    print(x, y, z)
    mx = 2 ** 16 - 1
    if x > mx or y > mx or z > mx:
        print("Value exceeded max")
        return
    data = [
        16,
        x >> 8,
        (x & 0b0000000011111111),
        y >> 8,
        (y & 0b0000000011111111),
        z >> 8,
        (z & 0b0000000011111111),
    ]
    print(motor_controller.send_command(data))


if __name__ == '__main__':
    motor_controller = MotorController(busy_line=21)
    motor_controller.send_command([0])
    run(0, 1000, 0)
    run(5000, 1000, 0)
    run(2500, 2500, 0)
    run(2400, 2500, 0)
    run(2400, 2400, 0)
    run(2500, 2400, 0)
    run(2500, 2500, 0)
    run(0, 0, 0)
    # while True:
    #     v = list(map(int, input('c: ').split(',')))
    #     run(v[0], v[1], v[2])
    # run(0,0,12000)
    # run(0, 0, 6000)
    # run(0, 0, 0)
    # try:
    #     run(15000, 0, 0)
    #     run(10000, 5000, 0)
    #     run(5000, 10000, 0)
    #     run(0, 0, 0)
    #     run(15000, 15000, 0)
    #     run(14000, 15000, 0)
    #     run(14000, 14000, 0)
    #     run(14000, 15000, 0)
    #     run(14000, 14000, 0)
    #     run(14000, 15000, 0)
    #     run(14000, 14000, 0)
    #     run(14000, 15000, 0)
    #     run(14000, 14000, 0)
    #     run(0, 0, 0)
    # except KeyboardInterrupt:
    #     pass


# 16,0,0,0,0,0,0
# 16,4,0,0,0,0,0

# 16384,8192,4096,2048,1024,512,256,128,64,32,16,8,4,2,1
#   0     0    0    0    0   0   0 | 0   0  0  0 0 0 0 0
