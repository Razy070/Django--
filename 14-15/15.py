# a = int(3)
# c = float(3.4)
# b = int(5)
# d = float(4.5)
#
# l = [
#     (a + d),
#     (c - b),
#     (b * c),
#     (d / a),
#     (a ** 2),
#     (a // 2),
#     (a % 2)]
#
# print("Список", l)
# print("Количество элементов в списке", len(l))
#
# l = list(map(int, input().split()))
# for i in l:
#     if int(i) % 2 == 0:
#         print(i)

###########################################

# def f(matrix) -> int:
#     n = min(len(matrix), len(matrix[0]))
#
#     s = 0
#     for i in range(n):
#         if (x := matrix[i][i]) % 2 == 0:
#             s += x
#     return s
#
#
# def main():
#     matrix = [
#         [3, 1, 1],
#         [1, 2, 1],
#         [1, 1, 3],
#     ]
#     print(f(matrix))
#
#
# if __name__ == '__main__':
#     main()

#################################################################

# First_name = str(input("Введите имя: "))
# Last_name = str(input("Введите фамилию: "))
#
# print("Меня зовут: " + First_name + " " + Last_name)
