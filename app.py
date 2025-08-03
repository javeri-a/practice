import random

def guess_the_number():
    print("Welcome! I'm thinking of a number between 1 and 10.")
    secret_number = random.randint(1, 10)

    while True:
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > 10:
            print("The number must be between 1 and 10.")
        elif guess < secret_number:
            print("Too low. Try a higher number.")
        elif guess > secret_number:
            print("Too high. Try a lower number.")
        else:
            print("Congratulations! You guessed it right 🎉")
            break

if __name__ == "__main__":
    guess_the_number()
