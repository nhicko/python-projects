# FOR ELSE & WHILE ELSE

search = [1, 2, 3, 4, 5, 6, 7]
target = 4

for element in search:
    if element == target:
        print('Found it!')
        break
else:
    print('I didn\'t find it!')

i = 0
while i < len(search):
    element = search[i]
    if element == target:
        print('found it')
        break
    i += 1
else:
    print('i didn\'t find it!')
