# emails = ['test@gmail.com', 'xyz@test.in', 'test@ya.ru', 'xyz@mail.ru', 'xyz@ya.ru', 'xyz@gmail.com']
# res = {}
# for i in emails:
#     a, b = i.split('@')
#     res[b] = res.get(b, 0) + 1
#
# print(*(f'{i}: {j}' for i, j in res.items()), sep='\n')

#####################################################

# test_list = ["all", "love", "and", "get", "educated", "by", "gfg"]
#
# # printing original list
# print("The original list is : " + str(test_list))
#
# res = []
# vow = "aeiou"
# for sub in test_list:
#     flag = False
#
#     # checking for begin char
#     for ele in vow:
#         if sub.startswith(ele):
#             flag = True
#             break
#     if flag:
#         res.append(sub)
#
# # printing result
# print("The extracted words : " + str(res))

##############################################

# import re
# text ='The quick brown\nfox jumps*over the lazy dog.'
# print(re.split('; |, |\*|\n',text))

