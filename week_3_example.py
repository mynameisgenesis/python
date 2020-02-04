from datetime import date

def validate_birth_year(year):
    if year > 1920 and year < date.today().year:
        return True
    else:
        return False


user_birth_year = int(input())

while not(validate_birth_year(user_birth_year)):
    print('Please enter a valid birth year.')
    user_birth_year = int(input())

if validate_birth_year(user_birth_year):
    print('Great! Thank you!')