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
