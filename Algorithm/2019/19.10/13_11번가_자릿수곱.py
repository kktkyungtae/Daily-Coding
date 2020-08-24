# 11번가

# 주어진 숫자를 1 에서 10 사이의 진수로 변경하고
# 각 자리 수의 곱하였을 때
# 그 숫자가 가장 큰 수와, 변환한 진수를 출력해라

def solve(n):
    result = [0, 0]
    for i in range(2, 10):
        temp = n
        temp_li = [1]

        while temp > 1:
            temp_li.append(temp % i)
            temp //= i

        ans = 1

        for k in range(len(temp_li)):
            if temp_li[k] != 0:
                ans *= temp_li[k]

        if result[1] <= ans:
            result[1] = ans
            result[0] = i

    return result

print(solve(10))