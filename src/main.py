"""
Password Generator (CLI)
Generates secure random passwords using Python secrets module.

Author: Michel Brochu
Version: 1.0 (2026)
"""

import secrets, string, argparse

def generate_password(length: int, use_digits: bool) -> str:
    alphabet = string.ascii_letters
    if use_digits:
        alphabet += string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))

def parse_args():
    parser = argparse.ArgumentParser(description="Secure password generator")
    parser.add_argument("--length", type=int, default=8)
    parser.add_argument("--no-digits", action="store_true", help="Disable digits")
    return parser.parse_args()

def main():
    args = parse_args()
    password = generate_password(args.length, use_digits=not args.no_digits)
    print(password)

if __name__ == "__main__":
    main()
