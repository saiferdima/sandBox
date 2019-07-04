import simplecrypt

encrypted = open("encrypted.bin", "rb").read()
passwords = open("passwords.txt").readlines()

for p in passwords:
    p = p.strip()
    try:
        print(simplecrypt.decrypt(p, encrypted))
    except simplecrypt.DecryptionException:
        continue
