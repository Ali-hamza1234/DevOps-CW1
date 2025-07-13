# Dec2Hex.py
#Final push for CI/CD demo
def decimal_to_hex(decimal_value):
    if not isinstance(decimal_value, int):
        raise ValueError("Input must be an integer")

    hex_chars = '0123456789ABCDEF'
    hexadecimal = ""

    print(f"Converting the Decimal Value {decimal_value} to Hex...")

    num = decimal_value
    if num == 0:
        return "0"

    while num > 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal
        num //= 16

    print(f"Hexadecimal representation is: {hexadecimal}")
    return hexadecimal

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        try:
            decimal_value = int(sys.argv[1])
            decimal_to_hex(decimal_value)
        except ValueError:
            print("Please provide a valid integer.")
    else:
        print("Usage: python Dec2Hex.py <decimal_number>")

