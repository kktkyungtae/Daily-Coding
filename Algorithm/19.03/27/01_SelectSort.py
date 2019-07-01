a = [489,29,3,1,34,53,2,4,5,3,44]

def SelectSort(a): # a is wanted Sorting arr
    n = len(a)
    for i in range(0,n-1):
        min = i
        for j in range(i+1,n):
            if a[min] > a[j]:
                min = j
        temp = a[min]
        a[min] = a[i]
        a[i] = temp
    return a


# def SelectSort(a):
#     if len(a) <= 1:
#         return a
#     else:
#         min_idx = a.index(min(a))
#         return [a.pop(min_idx)] + SelectSort(a)

print(SelectSort(a))