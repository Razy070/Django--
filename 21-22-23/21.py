# i = 'rGMTLIVrHIQSGIEWIVGIEWIV'  # int(input(любое слово))
# a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# for k in range(len(a)):
#     transformation = ''
#     for s in i:
#         if s in a:
#             n = a.find(s)
#             n = n - k
#             if n < 0:
#                 n = n + len(a)
#             transformation = transformation + a[n]
#
#         else:
#             transformation = transformation + s
# print('Hacking k #%s: %s' % (k, transformation))


#########################################################
#
# x = 'banana , apple, bananamango, mango, strawberry-banana'
# y = str(input('введите название фрукта:'))
# v2 = x.count(y)
# print('фруктов', y, 'было:', v2)


########################################################

# tuple_1 = ('1', '2', '3', '4', '5', '1', '1', '1')
#
#
# def tuple_replace(tuple_input, old_word, new_word):
#     return tuple([new_word if i == old_word else i for i in list(tuple_input)])
#
#
# print(tuple_replace(tuple_1, '1', '6'))
