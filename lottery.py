import os
import json
from random import random
from random import randrange

# создание игрового поля для дальнейшей генерации билета лото
def play_field():
# создание и заполнение массива с неповторяющимися числами для заполнения игровых полей
    numbers_for_filling = [[] for i in range(10)]
    for i in range(len(numbers_for_filling)):
        numbers_for_filling[i] = [j+i*10 for j in range(10)]
        numbers_for_filling[i] = sorted(numbers_for_filling[i], key=lambda x:random())
    numbers_for_filling[0].remove(0)
# создаем и заполняем игровое поле числами, сортируем их последовательно для удобство просмотра
    play_field=[[],[],[],[],[],[]]
    for i in range(6):
        random_place = [i for i in range(9)]
        random_place = sorted(random_place, key=lambda x:random())
        play_field[i] = [numbers_for_filling[random_place[j]].pop() for j in range(6)]
        play_field[i].sort()
    return(play_field)

# создание билета лото
def ticket():
    ticket_play_field = play_field()
    ticket_number = 'T-{0:0>3}-{1:0>7}'.format(randrange(1,999), randrange(1,9999999))
    ticket = {'number' : ticket_number, 'draw' : 1, 'play_field' : ticket_play_field}
    return(ticket)

# массовая генерация билетов лото и запись их в текстовые файлы
def tickets_generation():
    for i in range(1):
        generated_ticket = ticket()
        file_temp = open(r'tickets/' + generated_ticket['number'] + '.txt','w')
        json.dump(generated_ticket, file_temp)
    file_temp.close()

# создание пула боченков и его запись в тектовый файл
def barrels_generation():
    numbers = [i for i in range(1,100)]
    numbers = sorted(numbers, key=lambda x:random())
    numbers = numbers[:80]
    numbers.sort()
    file_temp = open(r'barrels.txt','w')
    json.dump(numbers, file_temp)
    file_temp.close()

# проверка билета на выигрыш
def ticket_check(ticket):
    file_temp = open(r'barrels.txt','r')
    barrels = json.load(file_temp)
    file_temp.close()
    row = 0
    match_in_row = 0
    match_in_bracket = 0
    win_low_tier = 0
    win_high_tier = 0

    for i in ticket['play_field']:
        row += 1
# проверка на совпадение в строке
        for j in i:
            if j in barrels:
                match_in_row += 1
        if match_in_row == 6:
            match_in_bracket += 1
            win_low_tier += 1
        match_in_row = 0
# проверка на малый и большой выигрыш
        if row %3 == 0 and match_in_bracket == 3:
            win_high_tier = 1
        if row %3 == 0:
            match_in_bracket = 0
        if win_low_tier == 6:
            win_high_tier = 2

    if win_high_tier == 2:
        prize = '1 000 000 rub'
    elif win_high_tier == 1:
        prize = '50 000 rub'
    else:
        prize = str(win_low_tier*100) + ' rub'
    return('{0} - {1}'.format(ticket['number'], prize))

# проверка сгенерированных билетов на выигрышь и составление файла с отчетом
def report():
    report = []
    for i in os.listdir('tickets'):
        file_temp = open(r'tickets/' + i,'r')
        ticket = json.load(file_temp)
        file_temp.close()
        report.append(ticket_check(ticket))
    file_temp = open(r'report.txt','w')
    json.dump(report, file_temp)
    file_temp.close()

# вывод отчета по выигрышам на экран
def print_report():
    file_temp = open(r'report.txt','r')
    report = json.load(file_temp)
    file_temp.close()
    no_win = 0
    low_win = 0
    win_50k = 0
    win_1m = 0
    for i in report:
        print(i)
        if i[16:] == '0 rub':
            no_win += 1
        if str.isdigit(i[16:19]) and int(i[16:19]) >= 100 and int(i[16:19]) <= 500:
            low_win += 1 
        if i[16:] == '50 000 rub':
            win_50k += 1
        if i[16:] == '1 000 000 rub':
            win_1m += 1
    print('\n{} не выигрышных билетов, {} билет(а) с выигрышом от 100 до 500 рублей,\n{} билет(а) с выигрышом 50 000 рублей и {} билет(а) с выигрышом 1 000 000 рублей'.format(no_win,low_win,win_50k,win_1m))

# вызов игровых функций
def start_game():
    if os.path.exists('tickets') == False:
        os.mkdir('tickets')
    for i in os.listdir('tickets'):
        os.remove('tickets/' + i)
    lottery_draw = input('How much tickets generate ? ')
    for i in range(int(lottery_draw)):
        tickets_generation()
    barrels_generation()
    report()
    print_report()

start_game()