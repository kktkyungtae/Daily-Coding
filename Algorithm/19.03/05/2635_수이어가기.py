nums = 100
result = []

for i in range(100):
    in_list = [nums, i]
    k = 0
    while True:
        minus = in_list[k] - in_list[k+1]
        if minus >= 0:
            in_list.append(minus)
            k += 1
        else:
            break