# Given a line of text as input, output the number of characters excluding spaces, periods, or commas.

import re
user_text = input()

''' Type your code here. '''
user_char_list = re.findall("[a-zA-Z0-9!]", user_text)
count = 0
for user_char in user_char_list:
    count += 1

print(count)