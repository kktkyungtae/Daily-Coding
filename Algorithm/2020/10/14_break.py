for i in range(10):
    if i % 2 == 0:
        break
        # 0이 짝수니까,, 0들어오자 마자 break해서 for문을 아예 나옴!!
        # break가 포함된 그 반복문만 깨고 나옴,, 다중 for문이면 다음 for문 실행
        print(i)
    else:
        print(i)
print("Done")

asa = ['a','b','c']
for i in range(10):
    if i % 2 == 0:
        print(i)
        for k in asa:
            if k == 'b':
                print(k)
                break
