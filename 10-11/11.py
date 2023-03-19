# n = int(input())
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# for i in range(n - 1):
#     sum -= int(input())
# print(sum)

#########################################

n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1
