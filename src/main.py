"""
Password Generator (CLI)
Generates secure random passwords using Python secrets module.

Author: Michel Brochu
Version: 1.0 (2026)
"""

import secrets, string, argparse

def generate_password(length: int, use_digits: bool, use_symbols: bool, use_upper: bool) -> str:
    alphabet = string.ascii_lowercase
    if use_digits:
        alphabet += string.digits

    if use_symbols:
        alphabet += "!@#$%^&*()-_=+[]{};:,.?/"

    if use_upper:
        alphabet += string.ascii_uppercase
    return "".join(secrets.choice(alphabet) for _ in range(length))

def parse_args():
    parser = argparse.ArgumentParser(description="Secure password generator")
    parser.add_argument("--length", type=int, default=8)
    parser.add_argument("--no-digits", action="store_true", help="Disable digits")
    parser.add_argument("--no-symbols", action="store_true", help="Disable symbols")
    parser.add_argument("--no-upper", action="store_true", help="Disable uppercase letters")
    return parser.parse_args()

def main():
    args = parse_args()
    password = generate_password(args.length, use_digits=not args.no_digits, use_symbols=not args.no_symbols, use_upper=not args.no_upper)
    print(password)

if __name__ == "__main__":
    main()
