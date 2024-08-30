import random

words = ["fire","desk","water","toy","bird","floor","python","shorts"
"cat","dog","table","hat","camp","jam","ram","gate","sack","yam","game","pad","rack"]

random_word = random.choice(words)

print('our random_word is ' + random_word)

print('******** WORD GUESSING GAME *******')

user_guesses = ''
chances = 10

while chances > 0:
    wrong_guesses = 0
    for character in random_word:
        if character in user_guesses:
            print(f"correct_guess: {character}")

        else:
            wrong_guesses += 1
            print('_') 
    if wrong_guesses == 0:
        print("correct")
        print(f"word : {random_word}")
        break
    guess = input("make a guess: ")
    user_guesses += guess

    if guess is not random_word:
        chances -= 1
        print(f"wrong.you have {chances} more chances")

        if chances == 0:
            print('game over')
