import random

n = random.randint(1,70)
print("I am the lottery number generator. I am thinking of a number between 1 and 70. ")

running = True
while running:
    guess_str = input("Take a guess. ")
    guess = int(guess_str)
    if guess == n:
        print("Well done, that is right!")
        running = False
    elif guess < n:
        print("Try a bigger number. ")
    else:
        print("Try a smaller number.")
