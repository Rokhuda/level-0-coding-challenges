def maximum_number(*args):
    max_num = 0
    for i in args:
        if i > max_num:
            max_num = i
    return max_num


print(maximum_number(10,4,7,10,30))