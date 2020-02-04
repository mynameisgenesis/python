user_input = input()
number_list = []
while not(user_input == 'quit' or user_input == 'Quit' or user_input == 'q'):
    number_list.append(int(user_input))
    user_input = input()

number_list.sort()
number_list_length = len(number_list) 
print(number_list[0], number_list[-1] )