import random
from words import words

print("🎮 Welcome to Hangman!")

# Select a random word
chosen_word = random.choice(words)

print("\nRandom word selected successfully!")

# For learning purposes only
print("Selected Word:", chosen_word)