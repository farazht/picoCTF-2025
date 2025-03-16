mappings = []
mascarpone = "MASCARPONE"
mascarpone_enc = input("Enter the encoded version of MASCARPONE: ")
pwd = input("Enter the password: ")

# find affine cipher values for A and B such that MASCARPONE encodes to the given encoded string
for i in range(26):
    for j in range(26):
        decoded = ""
        for c in mascarpone:
            decoded += chr(((ord(c) - 65) * i + j) % 26 + 65)
        if decoded == mascarpone_enc:
            mappings.append((i, j))

# try each mapping to decode the password
for i, j in mappings:
    decoded = ""
    for c in pwd:
        decoded += chr(((ord(c) - 65 - j) * pow(i, -1, 26)) % 26 + 65)
    print(decoded)