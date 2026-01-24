"""
Password Generator (CLI)
Generates secure random passwords using Python secrets module.

Author: Michel Brochu
Version: 1.0 (2026)
"""

import secrets, string

def generate_password(length: int) -> str:
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def main():
    length_text = input("Length? (e.g. 12): ")
    length = int(length_text)

    password = generate_password(length)
    print(password)


if __name__ == "__main__":
    main()
