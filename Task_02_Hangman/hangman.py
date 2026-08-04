import random
from words import words

print("=" * 50)
print("🎮 Welcome to Hangman Game")
print("=" * 50)

# Select a random word
chosen_word = random.choice(words)

# For learning only (Remove this later)
print("\nSelected Word:", chosen_word)

# Create hidden display
display = []

for letter in chosen_word:
    display.append("_")

print("\nHidden Word:")
print(" ".join(display))