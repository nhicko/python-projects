'''
Timed Math Generator
'''
import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 3


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
# FOR BEA
#    while True:
#        if left < right:
#            left = random.randint(MIN_OPERAND, MAX_OPERAND)
#        else:
#            break
# FOR BEA
    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0
input("Press Enter to start!")
print("---------------------")
start_time = round(time.time(), 2)

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
end_time = time.time()
total_time = end_time - start_time

print("---------------------")
print(f"Nice work, You finished in {total_time} seconds!")
