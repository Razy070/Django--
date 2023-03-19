# fib1 = 1
# fib2 = 1
#
# n = input("fibonacci number: ")
# n = int(n)
#
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
#
# print("fibonacci number:", fib2)


########################################################

n = int(input())
while n % 2 == 0 and n != 0: n //= 2
print(n == 1)
