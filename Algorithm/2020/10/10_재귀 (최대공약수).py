# 두 수의 최대공약수는 작은 수로 큰 수를 나누었을 때 남겨지는 나머지로
# 작은 수와 최대공약수를 구하는 것과 같다

def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

gcd(192,162)