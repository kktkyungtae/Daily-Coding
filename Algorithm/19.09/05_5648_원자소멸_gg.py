T = int(input())

# map으로 0.5만큰 움직이기
def move(i):
    dy, dx = d[i[2]]
    return [i[0]+dx, i[1]+dy, i[2], i[3]]

# dic에 i를 병합해주기 (key, value값을 유지하면서)
# i가 없어서 병합에 실패하면 except문 실행
# 즉, x,y가 같은, 원자들이 만나서 충돌하게되면 에너지값을 더해주기위해
# value에 i를 추가해줌

def dicts(i):
    x, y = i[0], i[1]
    try:
        dic[(x,y)].append(i)
    except:
        dic[(x,y)] = [i]

for tc in range(T):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    d = [(0.5,0), (-0.5,0), (0,-0.5), (0,0.5)]
    energy = 0
    for _ in range(4000):
        if(len(arr) < 2):
            break
        dic = {}
        arr = list(map(move, arr))
        list(map(dicts, arr))
        arr = []
        for i in dic:
          	# 원자들이 충돌해서 value값이 2개 이상일 때
            if(len(dic[i]) > 1):
                item = dic[i]
                for en in item:
                    energy += en[3]
            # value값이 1개일 때
            ## -1000 ~ 1000 범위 내에 있으면 arr에 다시 추가해줌
            else:
                item = dic[i]
                x = item[0][0]
                y = item[0][1]
                if(x < -1000 or x > 1000 or y < -1000 or y > 1000):
                    pass
                else:
                    arr.append(item[0])
    print("#{} {}".format(tc+1, energy))