# Baekjoon

# 숫자를 뒤집기 + (0)번째 버리기 해서 출력해라

tc = int(input())
for t in range(tc):
    func = list(input())
    lens = int(input())
    li_tmp = input()

    li = []
    for k in range(1, lens*2+1, 2):
        if ',' in li_tmp :
            li.append(li_tmp[k])
        else:

    #
    # if lens > 1:
    #     for i in func:
    #         if i == 'R':
    #             li.rweverse()
    #         else:
    #             li.pop()
    # elif lens == 1:
    #     if len(func) == 0:
    #         print(li_tmp)
    #         break
    #     else:
    #         print('error')
    #         break
    # else:
    #     print('error')

    print(li)
