import requests

key_word = 'We'


def get_first_word(s):
    word = s.split(' ')
    return word[0]


baseUrl = 'https://stepic.org/media/attachments/course67/3.6.3/'
link = 'https://stepic.org/media/attachments/course67/3.6.3/949017.txt'
flag = True
while flag:
    r = requests.get(link)
    string = str(r.text)
    print("String from File  = "+ string)
    word = get_first_word(string)
    if word == key_word:
        print(string)
        flag = False
        with open('output.txt', 'w') as file:
            file.write(string)
    else:
        link = baseUrl+string
