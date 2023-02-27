import random
secret_word = random.choice(["tracy", "code","run", "python" ])
guessed = []
wrong = []
tries =5   
while tries > 0:
    dashes = ""
    for letter in secret_word:
        if letter in guessed:
            dashes = dashes + letter
        else:
            dashes = dashes + "_"
    if dashes == secret_word:
        break
    print ("Guess the word:", dashes)
    print (tries, "chances left")
    guess = input()
    if guess in guessed or guess in wrong:
        print("Already guessed", guess)
    elif guess in secret_word:
        print ("Yay")
        guessed.append(guess)
    else:
        print ("Nope")
        tries = tries - 1
        wrong.append(guess)
    print()
def get_guess():
 if tries:
    print("You Won! The is "+secret_word)
 else:
    print("You Lose! The word is "+secret_word)
get_guess()