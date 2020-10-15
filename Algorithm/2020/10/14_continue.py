for i in range(10):
    if i % 2 == 0:
        # 2의 배수면 continue가 발동해서,, 해당 if문의 print랑
        continue
        print(i)
    print(i) # 얘도 넘어가버려! 바로 다음 index의 for문이 돌아가
print("Done")