b = []
while True:
    b = int(input('chislo:'))
    if sum(b) == 0:
        break
print([i * i for i in b])
