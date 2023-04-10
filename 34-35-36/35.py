def plus_two(number):
    # в number ожидается число
    # в ином случае должна выбрасываться ошибка
    try:
        print(2 + number)
    except TypeError:
        print('Ожидаемый тип данных — число!')


number = '2 плюс 2'
plus_two(number)
