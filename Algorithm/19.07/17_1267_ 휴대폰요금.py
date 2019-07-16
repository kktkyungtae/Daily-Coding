# 백준
# 휴대폰 요금
# Y 요금제 30초 마다 10원
# M 요금제 60초 마다 15원
# 입력>
# 통화 갯수
# 출력>
# Y, M 중에 싼 요금제가 뭔지랑 얼마인지
# 만약 같으면 Y,M 출력하고 요금

tc = int(input())
call_li = list(map(int,input().split()))

y_sum , m_sum = 0, 0

for i in call_li:
    y_sum += (i//30 + 1) * 10
    m_sum += (i//60 + 1) * 15

if y_sum < m_sum:
    print('Y', y_sum)
elif y_sum > m_sum:
    print('M', m_sum)
else:
    print('Y M', y_sum)