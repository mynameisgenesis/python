''' Define your function here '''
# steps = int(input())

def steps_to_miles(user_steps):
    miles_walked = user_steps / 2000
    return miles_walked

if __name__ == '__main__':
    ''' Type your code here. '''
    print('{:.2f}'.format(steps_to_miles(input())))