import json
import os
# создание списков с странами участницыми и их результатами
countries=[{'name':'Russia',        'gold':0,'silver':0,'bronze':0},
           {'name':'Norway',        'gold':0,'silver':0,'bronze':0},
           {'name':'Canada',        'gold':0,'silver':0,'bronze':0},
           {'name':'USA',           'gold':0,'silver':0,'bronze':0},
           {'name':'Netherland',    'gold':0,'silver':0,'bronze':0},
           {'name':'Germany',       'gold':0,'silver':0,'bronze':0},
           {'name':'Switzerland',   'gold':0,'silver':0,'bronze':0},
           {'name':'Belarus',       'gold':0,'silver':0,'bronze':0},
           {'name':'France',        'gold':0,'silver':0,'bronze':0},
           {'name':'Austria',       'gold':0,'silver':0,'bronze':0}]
results=[[{'sport':'1.1',   'gold':'Netherland',    'silver':'Norway',          'bronze':'Austria'},
          {'sport':'1.2',   'gold':'Germany',       'silver':'Norway',          'bronze':'Norway'},
          {'sport':'1.3',   'gold':'Austria',       'silver':'Russia',          'bronze':'Austria'}],
         [{'sport':'2.1',   'gold':'Austria',       'silver':'USA',             'bronze':'Austria'},
          {'sport':'2.2',   'gold':'Austria',       'silver':'Russia',          'bronze':'France'},
          {'sport':'2.3',   'gold':'Norway',        'silver':'Switzerland',     'bronze':'Switzerland'}],
         [{'sport':'3.1',   'gold':'Norway',        'silver':'Switzerland',     'bronze':'Switzerland'},
          {'sport':'3.2',   'gold':'Norway',        'silver':'Austria',         'bronze':'USA'},
          {'sport':'3.3',   'gold':'Germany',       'silver':'Russia',          'bronze':'Switzerland'}],
         [{'sport':'4.1',   'gold':'Switzerland',   'silver':'Russia',          'bronze':'Canada'},
          {'sport':'4.2',   'gold':'Netherland',    'silver':'Russia',          'bronze':'Netherland'},
          {'sport':'4.3',   'gold':'Germany',       'silver':'Germany',         'bronze':'Netherland'}],
         [{'sport':'5.1',   'gold':'France',        'silver':'USA',             'bronze':'France'},
          {'sport':'5.2',   'gold':'Germany',       'silver':'Canada',          'bronze':'Austria'},
          {'sport':'5.3',   'gold':'Germany',       'silver':'Canada',          'bronze':'France'}],
         [{'sport':'6.1',   'gold':'Russia',        'silver':'Canada',          'bronze':'Norway'},
          {'sport':'6.2',   'gold':'Russia',        'silver':'Germany',         'bronze':'Austria'},
          {'sport':'6.3',   'gold':'Russia',        'silver':'Belarus',         'bronze':'France'}],
         [{'sport':'7.1',   'gold':'Netherland',    'silver':'Austria',         'bronze':'Norway'},
          {'sport':'7.2',   'gold':'Austria',       'silver':'Netherland',      'bronze':'Netherland'},
          {'sport':'7.3',   'gold':'France',        'silver':'Norway',          'bronze':'France'}],
         [{'sport':'8.1',   'gold':'USA',           'silver':'USA',             'bronze':'Norway'},
          {'sport':'8.2',   'gold':'Switzerland',   'silver':'France',          'bronze':'Belarus'},
          {'sport':'8.3',   'gold':'Switzerland',   'silver':'Belarus',         'bronze':'Belarus'}],
         [{'sport':'9.1',   'gold':'France',        'silver':'Norway',          'bronze':'Germany'},
          {'sport':'9.2',   'gold':'Netherland',    'silver':'Austria',         'bronze':'Canada'},
          {'sport':'9.3',   'gold':'Netherland',    'silver':'Germany',         'bronze':'Germany'}],
         [{'sport':'10.1',  'gold':'Germany',       'silver':'Norway',          'bronze':'Canada'},
          {'sport':'10.2',  'gold':'Russia',        'silver':'Norway',          'bronze':'Germany'},
          {'sport':'10.3',  'gold':'France',        'silver':'Norway',          'bronze':'Russia'}],
         [{'sport':'11.1',  'gold':'Austria',       'silver':'Netherland',      'bronze':'Canada'},
          {'sport':'11.2',  'gold':'Russia',        'silver':'Switzerland',     'bronze':'USA'},
          {'sport':'11.3',  'gold':'Germany',       'silver':'Belarus',         'bronze':'Switzerland'}],
         [{'sport':'12.1',  'gold':'Switzerland',   'silver':'USA',             'bronze':'Switzerland'},
          {'sport':'12.2',  'gold':'Switzerland',   'silver':'France',          'bronze':'Russia'},
          {'sport':'12.3',  'gold':'Austria',       'silver':'Netherland',      'bronze':'France'}],
         [{'sport':'13.1',  'gold':'USA',           'silver':'Belarus',         'bronze':'France'},
          {'sport':'13.2',  'gold':'Netherland',    'silver':'Canada',          'bronze':'Belarus'},
          {'sport':'13.3',  'gold':'USA',           'silver':'Canada',          'bronze':'Canada'}],
         [{'sport':'14.1',  'gold':'USA',           'silver':'Belarus',         'bronze':'Switzerland'},
          {'sport':'14.2',  'gold':'USA',           'silver':'Canada',          'bronze':'Switzerland'},
          {'sport':'14.3',  'gold':'France',        'silver':'Netherland',      'bronze':'USA'}],
         [{'sport':'15.1',  'gold':'Norway',        'silver':'USA',             'bronze':'USA'},
          {'sport':'15.2',  'gold':'Norway',        'silver':'Austria',         'bronze':'Belarus'},
          {'sport':'15.3',  'gold':'Austria',       'silver':'Austria',         'bronze':'USA'}],
         [{'sport':'16.1',  'gold':'Austria',       'silver':'Netherland',      'bronze':'Belarus'},
          {'sport':'16.2',  'gold':'Switzerland',   'silver':'Netherland',      'bronze':'Germany'},
          {'sport':'16.3',  'gold':'Switzerland',   'silver':'Switzerland',     'bronze':'Germany'}]]
# подсчет результатов по странам и формирования файлов с отчетами
def backup_report(days_have_passed):
    if os.path.exists('results') == False:
        os.mkdir('results')
    for i in os.listdir('results'):
        os.remove('results/' + i)
    for i in range(int(days_have_passed)):
        for j in range(len(results[i])):
            for k in range(len(countries)):
                if results[i][j]['gold'] == countries[k]['name']:
                    countries[k]['gold'] = countries[k]['gold'] + 1
                if results[i][j]['silver'] == countries[k]['name']:
                    countries[k]['silver'] = countries[k]['silver'] + 1
                if results[i][j]['bronze'] == countries[k]['name']:
                    countries[k]['bronze'] = countries[k]['bronze'] + 1
        file_temp = open(r'results/day_' + str('{0:0>2}'.format(i + 1)) + '.txt','w')
        json.dump(results[i], file_temp)
        file_temp.close()
    file_temp = open(r'' + str('{0:0>2}'.format(days_have_passed)) + '_days_report' + '.txt','w')
    json.dump(countries, file_temp)
    file_temp.close()
# сортировка по медалям и их значимости
def sort():
    for i in range (1, len(countries)):
        j = i
        while j > 0 and countries[j]['gold'] > countries[j-1]['gold']:
            countries[j],countries[j-1] = countries[j-1],countries[j]
            j = j - 1
    for i in range (1, len(countries)):
        if countries[i]['gold'] == countries[i-1]['gold']:
            if countries[i]['silver'] > countries[i-1]['silver']:
                countries[i],countries[i-1] = countries[i-1],countries[i]
                i = i - 1
    for i in range (1, len(countries)):
        if countries[i]['silver'] == countries[i-1]['silver']:
            if countries[i]['bronze'] > countries[i-1]['bronze']:
                countries[i],countries[i-1] = countries[i-1],countries[i]
                i = i - 1
# вывод результатов на экран консоли
def results_print():
    print('\n{0:<12} {1:^7} {2:^7} {3:^7}\n'.format('Country','Gold','Silver','Bronze'))
    for i in range(len(countries)):
        print('{0:<12} {1:^7} {2:^7} {3:^7}'.format(countries[i]['name'],countries[i]['gold'],countries[i]['silver'],countries[i]['bronze']))

days_have_passed = input('How many days of olympic have passed ? ')
backup_report(days_have_passed)
sort()
results_print()