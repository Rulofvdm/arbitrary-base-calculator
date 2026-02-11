#!/usr/bin/env python3
"""
Divide number1 by number2 in a given base.
Prints the quotient and remainder.
"""

import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: python divide.py <base> <number1> <number2>")
        print("Example: python divide.py 10 17 5   → quotient 3, remainder 2")
        print("Example: python divide.py 16 FF 10 → quotient 25, remainder 5")
        sys.exit(1)

    base = int(sys.argv[1])
    num1_str = sys.argv[2]
    num2_str = sys.argv[3]

    if base < 2 or base > 36:
        print("Error: base must be between 2 and 36")
        sys.exit(1)

    try:
        num1 = int(num1_str, base)
        num2 = int(num2_str, base)
    except ValueError as e:
        print(f"Error: invalid number for base {base}: {e}")
        sys.exit(1)

    if num2 == 0:
        print("Error: division by zero")
        sys.exit(1)

    quotient = num1 // num2
    remainder = num1 % num2

    print(f"Quotient:  {quotient} (decimal)")
    print(f"Remainder: {remainder} (decimal)")

    if base != 10:
        print(f"\nIn base {base}:")
        print(f"  Quotient:  {np_base(quotient, base)}")
        print(f"  Remainder: {np_base(remainder, base)}")


def np_base(n: int, base: int) -> str:
    """Convert non-negative int to string in given base (2–36)."""
    if n == 0:
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    while n:
        result.append(digits[n % base])
        n //= base
    return "".join(reversed(result))


if __name__ == "__main__":
    main()
