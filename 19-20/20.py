# a = ['da', 'net', 'poka']
# b = len(max(a))
#
# for i in range(len(a)):
#     c = b-len(a[i])
#     print("*" * c + str(a[i]))

##########################################
import random

N = random.randint(1, 10)
arr = [random.randint(-100, 100)
       for i in range(N)]
print(arr)
sum_pl = 0
sum_ml = 0

for i in range(N):
    if arr[i] > 0:
        sum_pl += arr[i]
    elif arr[i] < 0:
        sum_ml += arr[i]
print("sum plus number=" + str(sum_pl))
print("sum minus number=" + str(-sum_ml))

if sum_pl > -sum_ml:
    arr.append(-(sum_ml + sum_pl))
elif sum_pl < -sum_ml:
    arr.append(-(sum_pl + sum_ml))
print(arr)
