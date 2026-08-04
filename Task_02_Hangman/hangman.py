import random
from words import words

print("=" * 50)
print("🎮 Welcome to Hangman Game")
print("=" * 50)

# Select random word
chosen_word = random.choice(words)

# Create hidden display
display = []

for letter in chosen_word:
    display.append("_")

print("\nHidden Word:")
print(" ".join(display))

# --------------------------
# Player Guess
# --------------------------

guess = input("\nGuess a letter: ").lower()

# Check if guessed letter exists
for position in range(len(chosen_word)):
    letter = chosen_word[position]

    if letter == guess:
        display[position] = guess

print("\nUpdated Word:")
print(" ".join(display))