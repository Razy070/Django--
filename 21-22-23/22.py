# def superset(set_1, set_2):
#     if set_1 > set_2:
#         print(f'Объект {set_1} является чистым супермножеством')
#     elif set_1 == set_2:
#         print(f'Множества равны')
#     elif set_1 < set_2:
#         print(f'Объект {set_2} является чистым супермножеством')
#     else:
#         print('Супермножество не обнаружено')
#
# # Тесты
# set_1 = {1, 8, 3, 5}
# set_2 = {3, 5}
# set_3 = {5, 3, 8, 1}
# set_4 = {90, 100}
#
# superset(set_1, set_2)
# superset(set_1, set_3)
# superset(set_2, set_3)
# superset(set_4, set_2)


##################################################
# e3f = {
#     'dog',
#     'cat',
#     'walrus'
# }
#
# e2f = {
#   'dog': 'chien',
#   'cat': 'chat',
#   'walrus': 'morse'
# }
#
#
# print(e3f)
# print(e2f['dog'])

#####################################

# def set_gen(lst):
#
#     index = 0
#     while index < len(lst):
#         cnt = lst.count(lst[index])
#         if cnt > 1:
#             lst[index] = str(lst[index]) * cnt
#         index += 1
#
#     return set(lst)
#
# # Тесты
# list_1 = [1, 1, 3, 3, 1]
# list_2 = [5, 5, 5, 5, 5, 5, 5]
# list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
# print(set_gen(list_1))
# print(set_gen(list_2))
# print(set_gen(list_3))
