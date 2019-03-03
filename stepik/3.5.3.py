import requests

counter = 0
r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/764.txt')
with open('input.txt', 'w') as file:
    file.write(str(r.text))

with open('input.txt', 'r') as file:
    for line in file:
        counter = counter + 1

print(r.text)
print(counter)
