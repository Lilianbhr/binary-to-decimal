import sys
import os


def convert_binary_to_decimal(binary_number: str) -> int:
    """
    take a binary number of 8 bit and convert it to decimal
    :param binary_number: string (verified before using it as function's parameter)
    :return: integer (binary number converted)
    """
    pos = 7
    dec = 0
    for bit in binary_number:
        dec += int(bit) * 2 ** pos
        pos -= 1
    return dec


def convert_decimal_to_binary(decimal_number: int) -> str:
    """
    take a decimal number and convert it to binary (on 8 bits)
    :param decimal_number: integer (between 0 and 255, verified before using it as function's parameter)
    :return: string (decimal number converted)
    """
    binary = ""
    while decimal_number > 0:
        binary += str(decimal_number % 2)
        decimal_number //= 2
    for i in range(8 - len(binary)):
        binary += "0"
    return reverse(binary)


def reverse(chain: str) -> str:
    """
    take a string and reverse it
    :param chain: string
    :return: chain reversed
    """
    pos = -1
    result = ""
    for character in range(len(chain)):
        result += chain[pos - character]
    return result


def get_resource_path(relative_path: str) -> str:
    """
    construct resource's path by using _MEIPASS if project is compiled
    :param relative_path: string (resource's path from script's folder)
    :return: full path (useful when the project is compiled)
    """
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
