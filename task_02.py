cities = ['Москва', 'Канзасс', 'Сеул']
cities[0] = 34
cities[1] = 65
cities[2] = 87

q = input('Какой город (Москва Канзасс Сеул): ' )
if q == 'Москва':
    print(cities[0])

if q == 'Канзасс':
    print(cities[1]) 
    
if q == 'Сеул':
    print(cities[2])

all = input('Хотите узнать сколько всего людей?(да или нет)')

if all == 'да':
    print(cities[0] + cities[1] + cities[2])
    
elif all == 'нет':
    print('Ну и ладно...')

else :
    print('Пожалуйста,выберите да или нет')
    all = input ('Хотите узнать сколько всего людей?(да или нет)')
    if all == 'да':
         print (cities[0] + cities[1] + cities[2])
    
    elif all == 'нет':
        print ('Ну и ладно...')