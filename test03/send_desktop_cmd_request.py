import time
from test03 import base_tools
import requests

def clean_imei():
    base_imei = '0086002116510'
    url = 'http://t-3g.gionee.com/api/desktopentrycmd/cleanImeiById'
    for i in range(100):
        if i < 10:
            imei = base_imei + '0' + str(i)
        else:
            imei = base_imei + str(i)
        data = {
            'imei' : imei
        }
        r = requests.get(url, params=data)


def for_init_imei():
    base_imei = '0086002116510'
    with open('get_imei.txt', 'w') as fl:
        for i in range(50):
            if i < 10:
                imei = '%s0%s' % (base_imei, str(i))
            else:
                imei = '%s%s' % (base_imei, str(i))
            fl.write(imei + '\n')

    with open('not_get_imei.txt', 'w') as f2:
        for i in range(50, 100):
            imei = '%s%s' % (base_imei, str(i))
            f2.write(imei + '\n')

def get_imei_request(filename):
    data_null_count = 0
    data_list_empty_count = 0
    url = 'http://t-3g.gionee.com/api/desktopentrycmd/index'
    data = {'sysvs': '5.1.16',
            # 'imei': imei,
            'app_ver': '5.5.6',
            # 'version': int(time.time()),
            'nettype': '4',
            'api_key': '9dac6633be895da152187b9c1a5c0042',
            # 'api_sign': 'a74263c203dfb7c7b7632b38623b7d0c',
            'sdk_ver': '1.0',
            'model': 'M7',
            'andorid': '25'}
    with open(filename, 'r') as r1:
        all_imei = r1.readlines()
        print('all_imei:', all_imei.__len__())
        for imei in all_imei:
            imei = imei.strip('\n')
            data['imei'] = imei
            # data['version'] = str(int(time.time()))
            data['version'] = str(0)
            data['api_sign'] = base_tools.get_request_api_sign(data)
            r = requests.get(url, params=data)
            result = r.json()
            # print(result)
            if result['data']:
                if result['data']['list']:
                    li = result['data']['list']
                    if li.__len__:
                        i_str = '%s:' % imei
                        for i in li:
                            i_str = i_str + str(i['id']) + '_'
                    # if result['data']['list'][0]['id'] == 62:
                    #     print('imei:', imei)
                        print(i_str)
                else:
                    data_list_empty_count += 1
            else:
                data_null_count += 1
    # print('%s_%s:%d' % (filename, 'count', count))
    print('%s_%s:%d' % (filename, 'data_null_count', data_null_count))
    print('%s_%s:%d' % (filename, 'data_list_empty_count', data_list_empty_count))

if __name__ == '__main__':
    get_imei_request('get_imei.txt')
    get_imei_request('not_get_imei.txt')
