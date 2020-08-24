T = int(input())

for t in range(T):
    N = int(input())
    card = input()

    cnt_card = [0] * 10

    for c in card:
        for i in range(10):
            if c == str(i):
                cnt_card[i] += 1
                break

    max_cnt = 0
    max_idx = 0

    for j in range(len(cnt_card)):
        if cnt_card[j] >= max_cnt:
            max_cnt = cnt_card[j]
            max_idx = j

    print(f"#{t+1} {max_idx} {max_cnt}")