import random

number = random.randint(0, 50)

guess = ""

guess_count = 0

guess_limit = 20


print("You have 20 attempts to guess the number between 0 and 50. Good luck!")

while number != guess:
    if guess_count < guess_limit:
        guess = int(input("Enter a number: "))

        guess_count += 1
        if guess_count == 5:
            print("You've given it five great attempts! Keep going, you're doing well and might be close!")

        elif guess_count == 10:
            print("Good effort! Try another number.")

        elif guess_count == 15:
            print("Watch out, your attempts are running out! You have only 5 attempts left")

        if number == guess:
            print("Congratulations! You guessed the correct number!")

    else:
        print("oops, Game Over")
        print("You have used all your guesses")
        print(f"The Correct Number is {number}, Hard Luck")
        break




