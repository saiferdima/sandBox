first_keys = input()
second_keys = input()
convert = input()
revert = input()

codding = dict(zip(first_keys, second_keys))
decode = dict(zip(second_keys, first_keys))

for e in convert:
    print(codding.get(e), end='')
print('')

for e in revert:
    print(decode.get(e), end='')
