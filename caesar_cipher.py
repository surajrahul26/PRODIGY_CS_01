print("=== Caesar Cipher ===")

message = input("Enter message: ")
shift = int(input("Enter shift value: "))
mode = input("Encrypt or Decrypt? ").lower()

result = ""

for char in message:
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        if mode == "encrypt":
            result += chr((ord(char) - base + shift) % 26 + base)
        else:  # decrypt
            result += chr((ord(char) - base - shift) % 26 + base)
    else:
        result += char

print("Result:", result)
