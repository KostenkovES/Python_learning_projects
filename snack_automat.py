import os
import time

matrix_codes = [['A1','A2','A3'],
                ['B1','B2','B3'],
                ['C1','C2','C3'],
                ['D1','D2','D3']]
matrix_quantity = [[1,1,0],
                   [0,0,0],
                   [0,0,0],
                   [0,0,0]]
matrix_names = {'A1':'Coca-Cola',    'A2':'Pepsi-Cola',  'A3':'Fanta',
                'B1':'Sprite',       'B2':'7UP',         'B3':'Mountain Dew',
                'C1':'Snickers',     'C2':'Mars',        'C3':'Bounty',
                'D1':'Lays',         'D2':'Estrella',    'D3':'Pringles',}
back_seach = {'A':0,'B':1,'C':2,'D':3}

def work():
# очистка консоли
    os.system('cls')
# удаление наименования товара, если ячейка с товаром пуста
    for i in range(4):
        for j in range(3):
            if matrix_quantity[i][j] == 0:
                matrix_names[matrix_codes[i][j]] = ' '
# выведение на экран матрицы с товарами и их кодами
    for i in range(4):
        print('{0:^15} {1:^15} {2:^15}'.format(matrix_names[matrix_codes[i][0]],
                                        matrix_names[matrix_codes[i][1]],matrix_names[matrix_codes[i][2]]))

        print('{0:^15} {1:^15} {2:^15}\r'.format(matrix_codes[i][0],matrix_codes[i][1],matrix_codes[i][2]))
    
    buy = input('\nКакой товар вы хотите купить ? ')
# проверка товара на наличие и выдача товара
    if matrix_quantity[back_seach[buy[0]]][int(buy[1])-1] > 0:
        matrix_quantity[back_seach[buy[0]]][int(buy[1])-1] -= 1
        print('{0} {1}'.format('\nЗаберите',matrix_names[buy]))
    else:
        print('\nДанный товар отсутствует')
    time.sleep(2)

    quantity_check()
    if total_quantity == 0:
        os.system('cls')
        print('\n\n\nАвтомат пуст!')
        time.sleep(2)

# проверка автомата на общее количество товара    
def quantity_check():
    global total_quantity
    total_quantity = 0
    for i in range(4):
        for j in range(3):
            total_quantity += matrix_quantity[i][j]
    if total_quantity > 0:
        return True
    else:
        return False

while quantity_check() == True:
    work()