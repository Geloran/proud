from ast import operator
from timeit import repeat
from turtle import end_fill


l_m = ['январь', 'февраль', 'март', 'апрель ', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
l_m[0] = 31 
l_m[1] = 28
l_m[2] = 31
l_m[3] = 30
l_m[4] = 31
l_m[5] = 30
l_m[6] = 31
l_m[7] = 31
l_m[8] = 30
l_m[9] = 31
l_m[10] = 30
l_m[11] = 31


q = input('Введите номер месяца (от 1 до 12): ')
if q == '1':
    print(l_m[0])
elif q == '2':
    print(l_m[1], 'является високосным')
elif q == '3':
    print(l_m[2])
elif q == '4':
    print(l_m[3])
elif q == '5':
    print(l_m[4])
elif q == '6':
    print(l_m[5])
elif q == '7':
    print(l_m[6])
elif q == '8':
    print(l_m[7])
elif q == '9':
    print(l_m[8])
elif q == '10':
    print(l_m[9])
elif q == '11':
    print(l_m[10])
elif q == '12':
    print(l_m[11])
    print ('Спасибо.')
else:
    q = input('Введите повторно номер месяца (от 1 до 12): ')
    if q == '1':
        print(l_m[0])
    elif q == '2':
        print(l_m[1], 'является високосным')
    elif q == '3':
        print(l_m[2])
    elif q == '4':
        print(l_m[3])
    elif q == '5':
        print(l_m[4])
    elif q == '6':
        print(l_m[5])
    elif q == '7':
        print(l_m[6])
    elif q == '8':
         print(l_m[7])
    elif q == '9':
          print(l_m[8])
    elif q == '10':
        print(l_m[9])
    elif q == '11':
         print(l_m[10])
    elif q == '12':
        print(l_m[11])
        print ('Спасибо.')
    