
# Computer Architecture - Group 1
# Course Code: 25AIM34
# Signed Binary Arithmetic using 8-bit 2's Complement

BITS = 8


def to_8bit_binary(number):
    return format(number & 0xFF, '08b')


def signed_value(binary):
    value = int(binary, 2)

    if value >= 128:
        value -= 256

    return value


def signed_addition(a, b):
    binary_a = to_8bit_binary(a)
    binary_b = to_8bit_binary(b)

    unsigned_sum = int(binary_a, 2) + int(binary_b, 2)

    result_binary = format(unsigned_sum & 0xFF, '08b')
    result_decimal = signed_value(result_binary)

    overflow = (
        ((a >= 0) == (b >= 0))
        and ((result_decimal >= 0) != (a >= 0))
    )

    print("Operand A:", a, "->", binary_a)
    print("Operand B:", b, "->", binary_b)

    print("Binary Addition:")
    print(" ", binary_a)
    print("+", binary_b)
    print("-----------")
    print(" ", result_binary)

    print("Result in Decimal:", result_decimal)
    print("Arithmetic Overflow:", "Yes" if overflow else "No")
    print("-" * 40)


print("SIGNED 8-BIT BINARY ARITHMETIC")
print()

print("a) 120 + (+62)")
signed_addition(120, 62)

print("b) (-120) + (-62)")
signed_addition(-120, -62)


# Computer Architecture - Group 1
# Course Code: 25AIM34
# Logical Shift Operations on 8-bit Binary Numbers

BITS = 8


def logical_left_shift(binary, positions):
    print("Original 8-bit Binary:", binary)

    result = binary

    for step in range(1, positions + 1):
        result = result[1:] + '0'
        result = result[-BITS:].zfill(BITS)

        print(f"After left shift {step}: {result}")

    print("Final Result:", result)
    print("-" * 40)


def logical_right_shift(binary, positions):
    print("Original 8-bit Binary:", binary)

    result = binary

    for step in range(1, positions + 1):
        result = '0' + result[:-1]
        result = result[-BITS:].zfill(BITS)

        print(f"After right shift {step}: {result}")

    print("Final Result:", result)
    print("-" * 40)


print("a) Logical Left Shift")
logical_left_shift("10110110", 3)

print("b) Logical Right Shift")
logical_right_shift("11010100", 3)
