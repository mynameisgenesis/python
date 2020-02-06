# 4.15 LAB: Password modifier
# Many user-created passwords are simple and easy to guess. Write a program that takes a simple password and makes it stronger by replacing characters using the key below, 
# and by appending "q*s" to the end of the input string.

# i becomes !
# a becomes @
# m becomes M
# B becomes 8
# o becomes .
# Ex: If the input is:

# mypassword
# the output is:

# Myp@ssw.rdq*s
# Hint: Python strings are immutable, but support string concatenation. Store and build the stronger password in the given password variable.

# LAB
# ACTIVITY
# 4.15.1: LAB: Password modifier
# 0 / 10
import re

word = input()
password = ''

''' Type your code here. '''
password = re.sub("i", "!", word)
password = re.sub("a", "@", password)
password = re.sub("m", "M", password)
password = re.sub("B", "8", password)
password = re.sub("o", ".", password)

password = password + 'q*s'
print(password)