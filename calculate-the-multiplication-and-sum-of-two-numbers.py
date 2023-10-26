print('--- Calculate the multiplication and     ---')
print('--- sum of two number                    ---\n')


def compute(num1, num2):
    product = num1 * num2
    if int(product) <= 1000:
        return product
    else:
        return num1 + num2


num1 = 20
num2 = 30

num3 = 40
num4 = 30
print(compute(num1, num2))  # Expected result is 600
print()
print(compute(num3, num4))  # Expected result is 70
print()

print('--- Print the sum of the current number ---')
print('--- and the previous number             ---\n')

print('Printing current and previous number sum in a range(10)')
prev_num = 0
for i in range(10):
    sum = i + prev_num
    print(f'Current Number {i} Previous Number {prev_num} Sum: {sum}')
    prev_num = i

print('\n--- Print characters from a string that ---')
print('--- are present at an even index number ---\n')

str = input('Please input string: ')
str_len = len(str)
print(f'Original word is: {str}')

for i in range(0, len(str) - 1, 2):
    print(str[i])
print('\nUsing list slicing')
str_lst = list(str)
for i in str[0::2]:
    print(i)
