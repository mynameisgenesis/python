''' Type your code here. '''
user_input = input()
new_string = ''
for word in user_input.split():
    if word[0].isupper():
        new_string += word[0]
        
print(new_string)