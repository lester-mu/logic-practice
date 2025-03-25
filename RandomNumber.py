import random

low = 1
high = 100

guesses = 0
number = random.randint(low, high)


while True:
    guess = int(input(f"Enter a number between ({low} and {high}): "))

    guesses += 1

    if guess < number:
        print("Your number is low")
    elif guess > number:
        print("Your number is high")
    else:
        print("You got it")
        break

print(f"This round took you {guesses} times")

