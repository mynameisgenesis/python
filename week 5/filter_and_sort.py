def get_nums():
    user_list = []
    user_nums = list(map(int, input().split())) 
    user_list =  [abs(ele) for ele in user_nums]
    return sorted(user_list)

new_list = get_nums()
for i in new_list: 
    print(i, end=" ") 