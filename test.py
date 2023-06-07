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

print(binary_to_float("10001100"))