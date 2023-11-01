from typing import BinaryIO


def to_bytes(binary: int, byte_count: int = 1) -> bytes:
    return binary.to_bytes(byte_count, byteorder='big')


def translate_instruction(instruction: str) -> bytes:
    instruction = instruction.strip().split()
    if instruction[0] == 'home':
        return to_bytes(0b00000000, 1)
    if instruction[0] == 'move':
        x: int = int(instruction[1])
        y: int = int(instruction[2])
        z: int = int(instruction[3])
        flag: int = 0b0000
        if len(instruction) == 5:
            flag = int(instruction[4])
        code = 0b0001 << 4 | flag
        inst = code << (6 * 8)
        inst |= x << (4 * 8)
        inst |= y << (2 * 8)
        inst |= z
        return to_bytes(inst, 7)
    if instruction[0] == 'tool':
        flag: int = int(instruction[1])
        code = 0b0010 << 4 | flag
        return to_bytes(code)
    if instruction[0] == 'shift':
        x: int = int(instruction[1])
        x_sign: int = 0 if x >= 0 else 1
        x = abs(x)
        y: int = int(instruction[2])
        y_sign: int = 0 if y >= 0 else 1
        y = abs(y)
        z: int = int(instruction[3])
        z_sign: int = 0 if z >= 0 else 1
        z = abs(z)
        flag: int = 0b0000
        if len(instruction) == 5:
            flag = int(instruction[4])
        code = 0b0011 << 4 | flag
        inst = code << (6 * 8)
        inst |= (x | x_sign << 15) << (4 * 8)
        inst |= (y | (y_sign << 15)) << (2 * 8)
        inst |= z | (z_sign << 15)
        return to_bytes(inst, 7)
    if instruction[0] == 'cup':
        flag: int = int(instruction[1])
        code = 0b0100 << 4 | flag
        return to_bytes(code)
    if instruction[0] == 'paint':
        b: int = int(instruction[1])
        c: int = int(instruction[2])
        m: int = int(instruction[3])
        y: int = int(instruction[4])
        k: int = int(instruction[5])
        flag: int = 0b0000
        if len(instruction) == 7:
            flag = int(instruction[6])
        code = 0b0101 << 4 | flag
        inst = code << (10 * 8)
        inst |= b << (8 * 8)
        inst |= c << (6 * 8)
        inst |= m << (4 * 8)
        inst |= y << (2 * 8)
        inst |= k
        return to_bytes(inst, 11)


def translate_instructions(to_file: BinaryIO, instructions: str):
    for instruction in instructions.strip().split('\n'):
        to_file.write(translate_instruction(instruction))


def print_bytes_in_binary(data):
    """
    Print the binary representation of bytes in the input data.

    Args:
        data (bytes): The bytes to print in binary.
    """
    for byte in data:
        binary_representation = bin(byte)[2:].zfill(8)
        print(binary_representation)


file = open('example.mtm', 'wb')
ins = """
home
move 1 1 1
move 2 0 1 1
cup 3
home
paint 1200 200 300 0 0
"""
translate_instructions(file, ins)
