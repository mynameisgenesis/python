''' Define your function here. '''
def swap_values(user_val1, user_val2):   
    return user_val2, user_val1
    
if __name__ == '__main__': 
    ''' Type your code here. Your code must call the function. '''
    value_tuple = swap_values(int(input()), int(input()))
    print(value_tuple[0], value_tuple[1])