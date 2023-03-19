c1 = int(input())
c2 = int(input())
c3 = int(input())
c4 = int(input())
if (c1 + c2) % 2 == 0 and (c3 + c4) % 2 == 0:
    print('YES')
elif (c1 + c2) % 2 != 0 and (c3 + c4) % 2 != 0:
    print('YES')
else:
    print('NO')
    