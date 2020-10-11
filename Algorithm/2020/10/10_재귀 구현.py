# 동빈나

# 피보나치

def fibonach(n):
    if n <= 1:
        return 1
    else:
        return n * fibonach(n-1)

print(fibonach(4))