# ZIP Function tutorial

names = ['Tim', 'Joe', 'Billy', 'Sally']
ages = [21, 19, 18, 43]
eye_color = ['Blue', 'Brown', 'Green', 'Brown']

print(list(zip(names,ages,eye_color)))

for name, age, eye_color in zip(names, ages, eye_color):
    if age > 20:
        print(name)
    print(eye_color)
