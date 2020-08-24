import sys
sys.stdin = open("3_글자수.txt", "r")

T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()

    chk = 0
    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt += 1
        if(cnt>chk):
            chk = cnt
    print(f"#{t} {chk}")


