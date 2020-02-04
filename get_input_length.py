# 4.14 LAB: Count input length without spaces, periods, or commas
# Instructor note:
# Note: this section of your textbook contains activities that you will complete for points. To ensure your work is scored, please access this page 
# from the assignment link provided in Blackboard. If you did not access this page via Blackboard, please do so now.

# Given a line of text as input, output the number of characters excluding spaces, periods, or commas.

# Ex: If the input is:

# Listen, Mr. Jones, calm down.
# the output is:

# 21
# Note: Account for all characters that aren't spaces, periods, or commas (Ex: "r", "2", "!").

# LAB
# ACTIVITY
# 4.14.1: LAB: Count input length without spaces, periods, or commas
# 0 / 10

import re
user_text = input()

''' Type your code here. '''
user_char_list = re.findall("[a-zA-Z0-9!]", user_text)
count = 0
for user_char in user_char_list:
    count += 1

print(count)