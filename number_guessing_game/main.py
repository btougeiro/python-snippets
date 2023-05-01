import random
number = random.choice(range(1, 101))
level_options = ["easy", "normal", "hard", "expert", "godlike"]

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Choose a difficulty. Type {', '.join([l for l in level_options])}.")
level = input("> ")
while level not in level_options:
    print(f"Wrong answer. Type {', '.join([l for l in level_options])}.")
    level = input("> ")

if level == "easy":
    attempts = 10
elif level == "normal":
    attempts = 8
elif level == "hard":
    attempts = 5
elif level == "expert":
    attempts = 3
elif level == "godlike":
    attempts = 1

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    print("Make a guess")
    guess = int(input("> "))
    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    elif guess == number:
        print(f"You win! The number is {number}.")
        break
    attempts -= 1
else:
    print(f"Best luck next time! The number is {number}.")
    print("Game Over!")
