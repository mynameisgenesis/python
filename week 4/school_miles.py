''' Define your function here '''
def miles_to_laps(miles_run):
    laps_run = miles_run / 0.25
    print('{:.2f}'.format(laps_run))
    return laps_run

if __name__ == '__main__':
    ''' Type your code here. Your code must call the function. '''
    user_miles = float(input())
    miles_to_laps(user_miles)