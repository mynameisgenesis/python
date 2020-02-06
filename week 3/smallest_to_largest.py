user_input = input()
number_list = []

while not(user_input == 'quit' or user_input == 'Quit' or user_input == 'q'):
    if int(user_input) >= 0:
        number_list.append(int(user_input))
    user_input = input()
 
number_list.sort()
print(number_list[0], number_list[-1] )