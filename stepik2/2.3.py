import simplecrypt

import urllib
from urllib import request

# text = urllib.request.urlopen('https://stepic.org/media/attachments/lesson/24466/encrypted.bin').read().strip().decode()

# psw = urllib.request.urlopen('https://stepic.org/media/attachments/lesson/24466/passwords.txt').read().strip()
arr = []
f = open("./encrypted.bin")
# print(f.read())
# print(p.read())
#

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

passwords = open("passwords.txt").readlines()

for psw in passwords:
    psw = psw.strip()
    try:
        print(simplecrypt.decrypt(psw, encrypted))
    except simplecrypt.DecryptionException:
        print(psw, 'is wrong')
    else:
        print(psw, 'is correct')
