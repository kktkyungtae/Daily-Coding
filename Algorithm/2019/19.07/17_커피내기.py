print("오늘은 몇명입니까?")
num=int(input())
names = []
for _ in range(num):
    print(f'{_+1}번째 선수를 입력하시오.')
    names.append(input())

from random import randint
idx = randint(0,len(names)-1)
thx = names[idx]
names.pop(idx)
print("시작하시겠습니까?")
key = input()
import time
while names:
    time.sleep(3)
    na=names.pop()
    print(f'{na} 살았다!ㅋㅋㅋ')
print(f'{thx} 걸렸네 개꿀 ㅋㅋㅋ ')