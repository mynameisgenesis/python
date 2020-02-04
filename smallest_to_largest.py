# 4.18 LAB: Smallest and largest numbers in a list
# Write a program that reads a list of integers into a list as long as the integers are greater than zero, 
# then outputs the smallest and largest integers in the list.

# Ex: If the input is:

# 10
# 5
# 3
# 21
# 2
# -6
# the output is:

# 2 21
# You can assume that the list of integers will have at least 2 values.

# LAB
# ACTIVITY
# 4.18.1: LAB: Smallest and largest numbers in a list
# 0 / 10

user_input = input()
number_list = []
while not(user_input == 'quit' or user_input == 'Quit' or user_input == 'q'):
    number_list.append(int(user_input))
    user_input = input()

number_list.sort()
number_list_length = len(number_list) 
print(number_list[0], number_list[-1] )