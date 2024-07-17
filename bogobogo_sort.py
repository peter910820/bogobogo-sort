import random
x = input('print array, example: 2,6,3,4,6: ').split(',')
x = [int(int_x) for int_x in x]
result = sorted(x)
tmp = []
sort_number_amount, suffle = 2, 0
while tmp != result:
    tmp = []
    for _ in range(0, sort_number_amount):
        tmp.append(x[_])
    random.shuffle(tmp)
    print(tmp)
    suffle += 1
    print(f'suffle = {suffle}')
    j = False
    while j:
        for _ in range(1, sort_number_amount):
            if tmp[_-1] <= tmp[_]:
                continue
            else:
                j = True
                random.shuffle(tmp)
                print(tmp)
                suffle += 1
                print(f'suffle = {suffle}')
                break
    if len(tmp) != len(x): sort_number_amount += 1