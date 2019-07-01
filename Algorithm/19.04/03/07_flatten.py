import sys
sys.stdin = open('07_input.txt','r')

for tc in range(10):
    dump = int(input())

    box_list = list(map(int,input().split()))

    for i in range(dump):
        box_list[box_list.index(max(box_list))] -= 1
        box_list[box_list.index(min(box_list))] += 1

    print("#{} {}".format(tc+1, max(box_list) - min(box_list)))
