import hashlib
import getpass

print("CYBERSECURITY TOOLKIT")
print("--------------------")

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(not c.isalnum() for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"

def calculate_hash():
    filename = input("Enter file path: ")

    try:
        sha256 = hashlib.sha256()

        with open(filename, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                sha256.update(chunk)

        print("SHA-256:", sha256.hexdigest())

    except OSError:
        print("Unable to open the file.")

print("\n1. Password Strength Checker")
password = getpass.getpass("Enter password: ")
print("Password strength:", check_password(password))

print("\n2. File Hash Calculator")
calculate_hash()