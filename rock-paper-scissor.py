import random as r

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissor: ")
    computer = r.choice(['r', 'p', 's'])

    if(user == computer):
        return print(f'computer choose: {computer}\nits a tie')

    if(is_win(user, computer)):
        return print(f'computer choose: {computer}\nits a win')
    else:
        return print(f'computer choose: {computer}\nyou lose')

def is_win(player, opponent):
    #  r > s, p > r, s > p
    if ((player == 'r' and opponent == 's') or
        (player == 's' and opponent == 'p') or
        (player == 'p' and opponent == 'r')):
           return True
       
play()
