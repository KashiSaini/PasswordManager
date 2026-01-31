from vault import generate_key, encrypt, decrypt

generate_key()

msg = "hello123"

e = encrypt(msg)
d = decrypt(e)

print("Encrypted:", e)
print("Decrypted:", d)
