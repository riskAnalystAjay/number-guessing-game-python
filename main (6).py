import random

print("🎲 Welcome to the Number Guessing Game!")
secret = random.randint(1, 20)

while True:
    guess = int(input("Guess a number between 1 and 20: "))
    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! The number was", secret)
        break