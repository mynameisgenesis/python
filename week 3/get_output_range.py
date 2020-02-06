
# Gets two inputs as two integers. Outputs the first integer and subsequent increments of 10 as long as the value is less than or equal to the second integer.
num1 = int(input())
num2 = int(input())

if num2 < num1:
    print('Second integer can\'t be less than the first.')
elif num1 == num2:
    print(num1, end=' ')
    print('')
else:
    for i in range(num1, num2):
        while num1 <= num2:
            print(num1, end=' ')
            num1 += 10
    print('')