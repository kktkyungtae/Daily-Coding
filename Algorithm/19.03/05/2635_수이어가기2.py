N = 100

result = []

for n in range(N+1):
    temp_li = [N, n]
    i = 0
    while True:
        num = temp_li[i] - temp_li[i+1]
        if num >= 0:
            temp_li.append(num)
            i += 1
        else:
            break
    if len(result) < len(temp_li):
        result = temp_li

print(len(result))
print(' '.join([str(x) for x in result]))