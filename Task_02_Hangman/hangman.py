import random
from words import words
from hangman_art import stages


def play_game():

    print("=" * 50)
    print("🎮 Welcome to Hangman Game")
    print("=" * 50)

    # Select a random word
    chosen_word = random.choice(words)

    # Create hidden display
    display = ["_"] * len(chosen_word)

    # Game variables
    lives = 6
    guessed_letters = []

    # Main Game Loop
    while "_" in display and lives > 0:

        print("\nWord:")
        print(" ".join(display))

        print(f"\n❤️ Lives Remaining: {lives}")

        # Display Hangman Figure
        print(stages[lives])

        # Display guessed letters
        if guessed_letters:
            print("Guessed Letters:", " ".join(guessed_letters))
        else:
            print("Guessed Letters: None")

        # Take user input
        guess = input("\nGuess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single alphabet letter.")
            continue

        # Check duplicate guess
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Correct guess
        if guess in chosen_word:

            for position in range(len(chosen_word)):
                if chosen_word[position] == guess:
                    display[position] = guess

            print("✅ Correct Guess!")

        # Wrong guess
        else:
            lives -= 1
            print("❌ Wrong Guess!")

    # -------------------------
    # Game Result
    # -------------------------

    if "_" not in display:

        print("\nFinal Word:")
        print(" ".join(display))

        print("\n" + "=" * 50)
        print("🎉 CONGRATULATIONS!")
        print("=" * 50)
        print(f"You guessed the word: {chosen_word.upper()}")

    else:

        print(stages[0])

        print("\n" + "=" * 50)
        print("💀 GAME OVER!")
        print("=" * 50)
        print(f"The correct word was: {chosen_word.upper()}")
        print("Better luck next time!")


# -------------------------
# Play Again Loop
# -------------------------

while True:

    play_game()

    choice = input("\n🔄 Do you want to play again? (y/n): ").lower()

    if choice != "y":
        print("\n👋 Thank you for playing Hangman!")
        print("Have a great day!")
        break