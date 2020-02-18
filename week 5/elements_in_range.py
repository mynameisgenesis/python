''' Type your code here. '''
user_nums = list(map(int, input().split()))
min, max = map(int, input().split())
user_nums = sorted(user_nums)

for x in user_nums:
    if x >= min and x <= max:
        print(x, end=" ")