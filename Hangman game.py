import random
words = ["python", "apple", "computer", "program", "school"]
word = random.choice(words)
guessed = []
attempts = 6
while attempts > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print(display)
    if "_" not in display:
        print("You Win!")
        break
    guess = input("Enter a letter: ")
    if guess in word:
        guessed.append(guess)
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)
if attempts == 0:
    print("You Lost! Word was:", word)
    