# 4.17 LAB: Print string in reverse
# Write a program that takes in a line of text as input, and outputs that line of text in reverse. The program repeats, ending when the user enters "Quit", "quit", or "q" for the line of text.

# Ex: If the input is:

# Hello there
# Hey
# quit
# then the output is:

# ereht olleH
# yeH
# LAB
# ACTIVITY
# 4.17.1: LAB: Print string in reverse
# 0 / 10
user_input = input()
word_chars = []
word_backwards = []
new_words = []
while not(user_input == 'quit' or user_input == 'Quit' or user_input == 'q'):
    word_chars = list(user_input)

    for letter in word_chars:
        word_backwards[letter] -=1
        new_word = str(word_backwards)
    new_words.append(new_word)
print(word_chars)