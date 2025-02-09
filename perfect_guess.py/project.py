import random

n = random.randint(1, 100)  # Generate a random number
guesses = 0  

print(" Welcome to the Number Guessing Game! ")
print("I have chosen a number between 1 and 100. Try to guess it!")

while True:
    try:
        a = int(input("\nEnter your guess: "))
        guesses += 1  # Increment guesses once per loop

        if a > n:
            print(" Too high! Try a lower number.")
        elif a < n:
            print(" Too low! Try a higher number.")
        else:
            print(f" Congratulations! You guessed the number {n} correctly in {guesses} attempts! 🎉")
            break  # Exit the loop when the correct number is guessed
    except ValueError:
        print(" Invalid input! Please enter a valid number.")

