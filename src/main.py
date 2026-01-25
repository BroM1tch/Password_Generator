"""
Password Generator (CLI)
Generates secure random passwords using Python secrets module.

Author: Michel Brochu
Version: 1.0 (2026)
"""

import secrets, string, argparse

def generate_password(length: int) -> str:
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))

def parse_args():
    parser = argparse.ArgumentParser(description="Secure password generator")
    parser.add_argument("--length", type=int, default=8)
    return parser.parse_args()

def main():
    args = parse_args()
    password = generate_password(args.length)
    print(password)

if __name__ == "__main__":
    main()
