import random
from words import words

print("=" * 50)
print("🎮 Welcome to Hangman Game")
print("=" * 50)

# Select random word
chosen_word = random.choice(words)

# Create hidden display
display = ["_"] * len(chosen_word)

# Game variables
lives = 6
guessed_letters = []

while "_" in display and lives > 0:

    print("\nWord:")
    print(" ".join(display))

    print(f"\n❤️ Lives Remaining: {lives}")

    guess = input("Guess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet letter.")
        continue

    # Prevent duplicate guesses
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

    else:
        lives -= 1
        print("❌ Wrong Guess!")

# -------------------------
# Game Result
# -------------------------

if "_" not in display:
    print("\n🎉 Congratulations!")
    print("You guessed the word:", chosen_word)

else:
    print("\n💀 Game Over!")
    print("Correct word was:", chosen_word)