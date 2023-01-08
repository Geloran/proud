# Импорт библиотеки Pandas и файл
from google.colab import drive
drive.mount('/content/drive')

# Путь в папку
cd /content/drive/MyDrive/Colab Notebooks

# Вводим необходимые библиотеки
import pandas as pd
import cred
import numpy as np
info = pd.read_csv('info.csv', index_col='currency')
print(info)

#Добавим класс для получения данных по ссылке с дальнейшей обработкой
def get_data(mon):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={token}&interval={time}&apikey={cred.API_KEY}&datatype=csv'
    return pd.read_csv(url)

# Проверим
mon = 'AAPL'
#time = '60min'
df = get_data(mon)
print(df)
#df
#print(np.mean(df['close'][0:7]))
#print(df['close'][0:7])

#Первая функция
def give_num(mon):
  df = get_data(mon)
  MA_7 = np.mean(df['close'][0:7])
  MA_25 = np.mean(df['close'][0:25])
  if MA_7 >= MA_25:
    num = 1
  else:
    num = 0
  return num

#Конечная функция (Анализ и продажа/покупка)
def analyse(valu):
  num = give_num(valu)
  if info['position'][valu] != num:
    if num == 1:
      print(f'Для {valu}. Быстрая скользящая пересекла среднюю снизу вверх, КУПИТЬ!')
    elif num == 0:
      print(f'Для {valu}. Быстрая скользящая пересекла среднюю сверху вниз, ПРОДАВАТЬ!')
    info['position'][valu] = num
    return info
  else:
    if num == 1:
      print(f'Не время для продажи {valu}!')
    elif num == 0:
      print(f'Не время для покупки {valu}!')
    return
  
#Выведем финальный результат
for valu in info.index:
  trader(valu)
print(info)
