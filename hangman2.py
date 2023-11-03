import random

HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''', '''
 +---+
 O   |
     |
     |
    ===''', '''
 +---+
 O   |
 |   |
     |
    ===''', '''
 +---+
 O   |
/|   |
     |
    ===''', '''
 +---+
 O   |
/|\  |
     |
    ===''', '''
 +---+
 O   |
/|\  |
/    |
    ===''', '''
 +---+
 O   |
/|\  |
/ \  |
    ===''']

words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
        coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
        lion lizard llama mole monkey moose mouse mule newt otter owl panda
        parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
        skunk sloth snake spider stork swan tiger toad trout turkey turtle
        weasel whale wolf wombat zebra'''.split()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']

guess_word = []


def getRandomWord(wordList):
    #  This function returns a random string from the passed list of strings
    wordIndex = random.randint(0, len(wordList) - 1)
    print(words[wordIndex])
    guessed_word = words[wordIndex]
    while True:
        print(f'guess the word: {"_" * len(guessed_word)}')
        enter_word = input('enter a word: ')
        if enter_word not in alphabet:
            print('you entered invalid word, try again.')
        elif enter_word not in guessed_word:
            print('wrong.')
            alphabet.remove(enter_word)
        else:
            print('right')
    #  guess_word = set(words[wordIndex])
    #  print(f'guess word is {guess_word}')
    #  print([x for x in alphabet if x not in guess_word])


getRandomWord(words)
