def float_to_binary(number):
    if number == 0:
        return '0'

    binary = ''
    integer_part = int(float(number))
    decimal_part = float(number) - integer_part

    binary_integer = bin(integer_part)[2:]

    binary_decimal = ''
    while decimal_part > 0 and len(binary_decimal) < 5:
        decimal_part *= 2
        bit = int(decimal_part)
        binary_decimal += str(bit)
        decimal_part -= bit

    exponent = len(binary_integer) - 1
    biased_exponent = bin(exponent + 3)[2:].zfill(3)

    mantissa = (binary_integer[1:] + binary_decimal)[:5]
    mantissa = mantissa + (5 - len(mantissa)) * "0"

    binary = biased_exponent + mantissa
    return binary


def binary_to_float(binary):
    if binary == '0':
        return 0.0

    biased_exponent = int(binary[:3], 2)
    exponent = biased_exponent - 3

    mantissa = binary[3:]

    decimal_part = 0.0
    for i in range(len(mantissa)):
        decimal_part += int(mantissa[i]) * 2 ** -(i + 1)

    number = (1 + decimal_part) * 2 ** exponent

    return number

print(binary_to_float(float_to_binary("3.25")))