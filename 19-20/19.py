# n = int(input())
# arr = [int(input())
#        for _ in range(n)]
# a = sorted(arr, reverse=True)
# print(sum(a[::3]) + sum(a[1::3]))

##################################
num = [9, 4, 1, 6]
num.sort(reverse=True)
y = num[0]
result = []
for x in range(len(num) - 1):
    diff = num[x] - num[x + 1]
    if y == diff not in result:
        result.append([num[x + 1], num[x]])
    if diff < y:
        y = diff
        result = [[num[x + 1], num[x]]]
print(result)
