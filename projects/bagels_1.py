import random


def digitGenerator():
    return random.randint(0, 9)


def generateThreeDigits():
    digit1 = digitGenerator()
    digit2 = digitGenerator()
    digit3 = digitGenerator()

    return f"{digit1}{digit2}{digit3}"


def checkExistence(number: int, guess: int):
    pass


def main():
    print("I have thought up a number.")
    print("You have 10 guesses to get it.")

    guess = generateThreeDigits()
    print(f"this is the number i guessed {guess}")

    while True:
        user_input = int(input("Guess #1:"))
        if user_input < 100 or user_input > 999:
            print("number should be 3 digit")
        else:
            break

    # checking if the number exists in user_input
    # what is the position of the correct num!
    checkExistence(user_input, guess)


if __name__ == "__main__":
    main()
