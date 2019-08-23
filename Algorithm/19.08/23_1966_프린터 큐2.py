for _ in range(int(input())):
    array_size, index = map(int, input().split())
    value = list(map(int, input().split()))
    print_li = [0 for _ in range(array_size)]
    print_li[index] = 'T'

    count = 0
    while True:
        if value[0] == max(value):
            count += 1
            if print_li[0] == 'T':
                print(count)
                break
            else:
                value.pop(0)
                print_li.pop(0)
        else:
            value.append(value.pop(0))
            print_li.append(print_li.pop(0))