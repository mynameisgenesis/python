user_input = input()

user_chars = list(user_input.replace(" ", ""))
new_word = []
for char in reversed(user_chars):
    new_word.append(char)
    
if user_chars == new_word:
    print(user_input, 'is a palindrome')
else: 
    print(user_input, 'is not a palindrome')