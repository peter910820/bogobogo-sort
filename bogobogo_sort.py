import random
import time

x = input('print array, example: 2,6,3,4,6 : ').split(',')
x = [int(int_x) for int_x in x]
if len(x) <= 1:
    raise ValueError('List length cannot be less than or equal to 1')
timer_start = time.time()
result = sorted(x)
current_list = []
sort_number_amount, shuffle = 2, 0
while current_list != result:
    current_list = [x[index] for index in range(0, sort_number_amount)]
    random.shuffle(current_list)
    shuffle += 1
    print(current_list, f'shuffle = {shuffle}')
    j = False
    while j:
        for index in range(1, sort_number_amount):
            if current_list[index-1] <= current_list[index]:
                continue
            else:
                j = True
                random.shuffle(current_list)
                shuffle += 1
                print(current_list, f'shuffle = {shuffle}')
                break
    if len(current_list) != len(x):
        sort_number_amount += 1
    timer_end = time.time()
print(f'Time spent: {timer_end - timer_start}s')
