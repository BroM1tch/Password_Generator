"""
Password Generator (CLI)
------------------------
Generates secure random passwords using Python's secrets module.

This script is designed as a small CLI tool showcasing:
- secure randomness
- clean argument parsing
- input validation
- readable and maintainable structure

Author: Michel Brochu
Version: 1.0.0 (2026)
"""

import secrets, string, argparse

def generate_password(length: int, use_digits: bool, use_symbols: bool, use_upper: bool) -> str:
    alphabet = string.ascii_lowercase

    #Generate a secure random password based on selected character sets.
    if use_digits:
        alphabet += string.digits

    if use_symbols:
        alphabet += "!@#$%^&*()-_=+[]{};:,.?/"

    if use_upper:
        alphabet += string.ascii_uppercase

    if length < 4:
        raise ValueError("length must be >= 4")

    if not alphabet:
        raise ValueError("alphabet is empty (no character sets selected)")

    return "".join(secrets.choice(alphabet) for _ in range(length))

def parse_args():

    #Parse command-line arguments for the CLI.
    parser = argparse.ArgumentParser(description="Secure password generator")
    parser.add_argument("--length", type=int, default=8)
    parser.add_argument("--no-digits", action="store_true", help="Disable digits")
    parser.add_argument("--no-symbols", action="store_true", help="Disable symbols")
    parser.add_argument("--no-upper", action="store_true", help="Disable uppercase letters")
    parser.add_argument("-c", "--count", type=int, default=1, help="Number of passwords to generate (default: 1)")
    return parser.parse_args()

def main():
    """
    Program entry point.
    Handles validation and password generation loop.
    """
    args = parse_args()

    if args.count < 1:
        raise SystemExit("Error: count must be >= 1")

    for _ in range(args.count):
        try:
            password = generate_password(args.length, use_digits=not args.no_digits, use_symbols=not args.no_symbols, use_upper=not args.no_upper)
        except ValueError as e:
            raise SystemExit(f"Error: {e}")
        print(password)

if __name__ == "__main__":
    main()
