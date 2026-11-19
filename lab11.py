username = input("Enter your username: ")
password = input("Enter your password: ")

print("========================================")
print("PASSWORD VALIDATION REPORT")
print("========================================")
print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")

has_length = len(password) >= 8
has_digit = False
has_upper = False

for ch in password:
    if ch.isdigit():
        has_digit = True
    if ch.isupper():
        has_upper = True

print("")
print("--- Validation Rules ---")
if has_length:
    print(f"[PASS] Minimum 8 characters ({len(password)} characters)")
else:
    print(f"[FAIL] Minimum 8 characters ({len(password)} characters)")

if has_digit:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")

if has_upper:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")

print("")
print("--- Result ---")
if has_length and has_digit and has_upper:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID!")

print("")
print("========================================")
