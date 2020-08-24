# Baekjoon

# 제일 앞 카드를 버리고 다음 카드를 가장 뒤로 보내기를 반복해서
# 가장 마지막에 남는 카드를 출력해라

from collections import deque
num_ca = int(input())
cards = deque(i for i in range(1, num_ca + 1))

while len(cards) != 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])
