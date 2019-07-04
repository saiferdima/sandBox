import simplecrypt

import urllib
from urllib import request
#text = urllib.request.urlopen('https://stepic.org/media/attachments/lesson/24466/encrypted.bin').read().strip().decode()

#psw = urllib.request.urlopen('https://stepic.org/media/attachments/lesson/24466/passwords.txt').read().strip()
arr = []
f = open("./encrypted.bin")
# print(f.read())
# print(p.read())
#

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read().decode()


with  open("./passwords.txt") as p:

    for line in p:
        arr.append(line)

    for i in range(len(arr)):
        print (arr[i])
        try:  print(simplecrypt.decrypt(arr[i],encrypted))
        except:
            print ('wrong')







