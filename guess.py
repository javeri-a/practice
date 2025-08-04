import random

# Computer randomly chooses a number between 1 and 10
secret_number = random.randint(1, 10)

print("🎲 Welcome to the Number Guessing Game!")
print("Guess the number I'm thinking of between 1 and 10.")

# User gets 3 tries
for attempt in range(3):
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("🎉 Wah! Aap ne sahi guess kiya!")
        break
    elif guess < secret_number:
        print("📉 Aap ka guess chhota hai.")
    else:
        print("📈 Aap ka guess bara hai.")

else:
    print(f"😞 Maaf kijiye, aap haar gaye. Sahi number tha {secret_number}.")
