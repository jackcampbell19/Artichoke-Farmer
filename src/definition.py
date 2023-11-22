import random

from InstructionGenerator import InstructionGenerator as ig


def print_bytes_in_binary(arr):
    for num in arr:
        byte_representation = bin(num)[2:].zfill(8)  # Convert integer to binary and pad with zeros to make it 8 bits
        print(f"{byte_representation} ", end='')
    print()


def dip_paint_brush():
    return quick_z_speed() + [
        ig.move(None, None, 2000, False),
        ig.set_cup_holder_position(ig.CUP_HOLDER_POSITION_STANDARD),
        ig.move(None, None, 10000, False),
        ig.move(None, None, 8000, False),
        ig.move(None, None, 9000, False),
        ig.move(None, None, 2000, False),
        ig.set_cup_holder_position(ig.CUP_HOLDER_POSITION_HIDDEN),
    ] + normal_speed()


def paint_rectangle(x, y):
    z_clearance = 4000
    z_contact = 1200
    x0, y0 = x, y
    cmds = [
        ig.move(x0, y0, z_clearance, True),
        ig.move(x0, y0, z_contact, True)
    ]
    yr = 600
    xr = 70
    for i in range(5):
        cmds += [ig.move(x0, y0 + yr, z_contact, True)]
        x0 += xr
        cmds += [ig.move(x0, y0 + yr, z_contact, True)]
        cmds += [ig.move(x0, y0, z_contact, True)]
        x0 += xr
        cmds += [ig.move(x0, y0, z_contact, True)]
    cmds += [ig.move(x0, y0, z_clearance, True)]
    return cmds


def midpoint(x1, y1, x2, y2):
    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2
    return int(midpoint_x), int(midpoint_y)


def paint_line(x0, y0, x1, y1, dip):
    clearance = 2500
    contact = 1000
    light_contact = 2000
    mx, my = midpoint(x0, y0, x1, y1)
    cmds = [ig.move(mx, my, clearance, True)]
    if dip:
        cmds += dip_paint_brush()
    cmds += [
        ig.move(mx, my, light_contact, True),
        ig.move(x0, y0, contact, True),
        ig.move(x1, y1, contact, True),
        ig.move(mx, my, light_contact, True),
        ig.move(mx, my, clearance, True),
    ]

    return cmds


def quick_z_speed():
    return [ig.configure_speed(300, 80, 120)]


def normal_speed():
    return [ig.configure_speed(500, 120, 600)]


def generate_commands():
    cmds = [ig.configure_speed(500, 120, 600),]
    # cmds += [
    #     ig.configure_speed(500, 120, 600),
    #     ig.load_tool(2),
    #     ig.dispense_paint(50, 0, 0, 50, 50),
    #     ig.load_tool(2),
    # ]
    # cmds += [ig.wash_tool()]
    cmds += [ig.dispense_paint(0, 75, 0, 0, 0)]
    # cmds += [ig.load_tool(2)]
    for x in range(5):
        cmds += paint_line(
            random.randint(1000, 5000),
            random.randint(1000, 5000),
            random.randint(1000, 5000),
            random.randint(1000, 5000),
            x % 3 == 0
        )
    return cmds


if __name__ == '__main__':
    commands = generate_commands()
    for command in commands:
        print_bytes_in_binary(command)
