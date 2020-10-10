# 주어진 단어에서 알파벳이 몇개가 사용되었는지 출력해라

# 단어가 주어지더라도, str로 감싸서 받으면 한단어씩 띄워서 판단가능
words = list(map(str, input()))

# result = [0*i for i in range(26)]
# # 밑에꺼랑 같다
# # alphabets = []
# # for i in range(26):
# #     alphabets.append(0*i)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

results = []
for i in range(26):
    results.append(int(words.count(alphabet[i])))

for k in results:
    print(k, end = ' ')

