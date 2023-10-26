with open('sample.txt', 'r') as file:
    for i in file:
        data = file.read().replace('\n', ' ')
        print(data)
