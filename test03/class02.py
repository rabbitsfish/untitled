import requests
import time
url = 'http://t-osapi-3g.gionee.com/api/news_list/testGetConfig'
imei_base = '0086002116510'
# data = {
#     'sysvs' : '5.1.16',
#     'operators' : '',
#     'app_ver' : '5.5.6',
#     'nettype' : '1',
#     'pkg' : 'com.android.browser',
#     'cs' : '6291CF4CB91BA6A334E4E7420791F862',
#     'ver' : '1',
#     'android' : '5.1',
#     'model' : 'GN3001',
#     '__debug': 'zhi-pu__debug',
# }
count_dict = {}
data = {
    'module' : 'DEFAULT',
    'pkg' : 'com.android.browser'
}
imei_dict = {}

def select_count():
    for i in range(100):
        if i < 10:
            imei = imei_base + '0' + str(i)
        else:
            imei = imei_base + str(i)
        data['imei'] = imei
        r = requests.get(url, params=data)
        result = r.json()
        id = result['id']
        if id in count_dict.keys():
            count_dict[id]['count'] = count_dict[id]['count'] + 1;
        else:
            id_dict = {}
            id_dict['count'] = 1
            id_dict['percent'] = result['percent']
            id_dict['slow'] = result['slow']
            id_dict['percent_slow'] = result['percent_slow']
            id_dict['slow_times'] = result['slow_times']
            id_dict['slow_target_id'] = result['slow_target_id']
            id_dict['slow_execute_times'] = result['slow_execute_times']
            count_dict[id] = id_dict
    print(count_dict)


def slow_change_count():
    print('slow_change_count_if_00')
    for count in count_dict.keys():
        print('slow_change_count_if_0')
        id_dict = count_dict[count]
        if id_dict['slow'] == 1 and (id_dict['slow_times'] > id_dict['slow_execute_times']):
            print('slow_change_count_if_1')
            if id_dict['percent'] >= id_dict['percent_slow']:
                print('slow_change_count_if_2')
                slow_count = id_dict['percent_slow'] // \
                                     (id_dict['slow_times'] - id_dict['slow_execute_times'])
                print('slow_count:',  slow_count)
                id_dict['percent'] = id_dict['percent'] - slow_count
                print("percent:", id_dict['percent'])
                id_dict['slow_execute_times'] += 1
                id_dict['percent_slow'] = id_dict['percent_slow'] - slow_count
                count_dict[id_dict['slow_target_id']]['percent'] += slow_count

def imei_count():
    for i in range(100):
        if i < 10:
            imei = imei_base + '0' + str(i)
        else:
            imei = imei_base + str(i)
        data['imei'] = imei
        r = requests.get(url=url, params=data)
        result = r.json()
        id = result['id']
        if id in imei_dict.keys():
            imei_dict[id] = imei_dict[id] + 1
        else:
            imei_dict[id] = 1
    print('imei_dict:', imei_dict)


if __name__ == '__main__':
    select_count()
    slow_change_count()
    input('press anything to continue....')
    time.sleep(60)
    imei_count()
    for i in imei_dict.keys():
        if imei_dict[i] == count_dict[i]['percent']:
            print(i, imei_dict[i])
            print('yes')

        else:
            print('imei_dict[i]:', imei_dict[i])
            print('count_dict["percent"]', count_dict[i]['percent'])
            print('error')
