def get_nums():
    user_nums = list(map(int, input().split())) 
    return user_nums

def get_average(user_list):
    return round(sum(user_list) / len(user_list)) 

def largest_num(user_list):
    user_list.sort()
    return user_list[-1]

if __name__ == '__main__':
    list_of_nums = get_nums()
    print(get_average(list_of_nums), largest_num(list_of_nums))