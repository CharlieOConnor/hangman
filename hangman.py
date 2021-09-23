import random

def hangman():

    print("\nWelcome to hangman!")
    # Choose a random word from a text file
    with open("hangman.txt", "r") as file:
        allText = file.read()
        word = list(map(str, allText.split()))

    word_list = []
    chosen_word = random.choice(word)

    for i in range(len(chosen_word)):
        word_list.append(chosen_word[i])

    player_guesses = ["$" for i in range(len(word_list))]
    print(player_guesses)

    counter = 10

    # Keep the game going until either the player guesses the word or runs out of guesses
    while counter >= 1:
        user_guess = input("\nPlease enter a letter: ")

        if user_guess in word_list:
            for position, letter in enumerate(word_list):
                if letter == user_guess:
                    player_guesses[position] = letter
        else:
            print("You guessed incorrectly!")

        counter -= 1
        print("You have " + str(counter) + " guesse(s) left!")
        print("".join(player_guesses))

        if "$" not in player_guesses:
            print("You've guessed the word!")
            break

    if counter == 0:
        print("Oh dear, you've run out of guesses.")
        print("The word was: " + str("".join(word_list)))

player_choice = "y"

# Ask the player if they want to play again
while player_choice == "y":
    hangman()

    player_choice = input("\nDo you want to play again? (y/n): ")
