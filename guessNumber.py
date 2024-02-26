
import random

def main():

    startingPoint = None
    endPoint = None

    # print instructions and text to the terminal to start the script
    init()
    
    # ask the user for input of range where the script will randomly choose a number
    while True:
        try:
            inputRange = input("\nEnter a range to choose from (ex: 1-100): ")
            startingPoint, endPoint = inputRange.split('-')
            startingPoint = int(startingPoint)
            endPoint = int(endPoint)
        except ValueError:
            print("\nValueError: You must enter a valid range input! Try again.")
            continue

        gameRandomNumber = random.randint(startingPoint, endPoint)
        guess(gameRandomNumber)

        while True:
            print("\n+=====================================================+\n")
            loopInput = input("Do you want to play again? [Yes] or [No]: ").upper()

            if loopInput == "YES":
                print("\n+=====================================================+")
                break
            elif loopInput == "NO":
                print("\n\nThank you for playing! Till next time!\n")
                return
            else:
                print("You may only answer yes or no! Try again.\n")
                continue
        


def init():

    # prints to the terminal some visuals for the script
    print("\n+=====================================================+")
    print("|                                                     |")
    print("|                  Guess the Number!                  |")
    print("|               Simple Python Script Game             |")
    print("|                                                     |")
    print("+=====================================================+")


def guess(guessNumber):

    print("\n+=====================================================+\n")
    numberOfTries = 0
    guessInputNumber = None

    while numberOfTries < 5:
        try:
            guessInputNumber = input("What is your guess? ")
            guessInputNumber = int(guessInputNumber)
        except ValueError:
            print("Enter a valid guess integer!")
            continue

        if guessNumber == guessInputNumber:
            print("Wow! You've guessed the random number! Congratulations!\n")
            return
        elif guessInputNumber > guessNumber:
            print("Nice Try! Your guess was a little higher than the answer.\n")
        else:
            print("Damn that was close! Your guess was a little lower than the answer.\n")

        numberOfTries += 1

    print("\nYou've reached the maximum number of tries!")


if __name__ == "__main__":
    main()