from test03 import base_tools
import requests
count_dict = {}
def get_video():
    # url = 'http://3gosapi.3gtest2.gionee.com/api/video/list?sysvs=5.1.16&operators=&imei=61374BE70391D138C59679F7928FD8C9&app_ver=5.5.6&city=深圳&nettype=1&channel_id=YK__5210540&api_key=9dac6633be895da152187b9c1a5c0042&api_sign=23d624b9b22b83332985e7f3498ac66f&ver=1&model=M7&andorid=7.1.1'
    # url = 'http://3gosapi.3gtest2.gionee.com/api/video/list?sysvs=5.1.16&operators=&imei=61374BE70391D138C59679F7928FD8C9&app_ver=5.5.6&city=深圳&nettype=1&channel_id=YK__5210508&api_key=9dac6633be895da152187b9c1a5c0042&api_sign=23d624b9b22b83332985e7f3498ac66f&ver=1&model=M7&andorid=7.1.1'
    url = 'http://3gosapi.3gtest2.gionee.com/api/video/list?sysvs=5.1.16&operators=&imei=61374BE70391D138C59679F7928FD8C9&app_ver=5.5.6&city=深圳&nettype=1&channel_id=YK__5210542&api_key=9dac6633be895da152187b9c1a5c0042&api_sign=23d624b9b22b83332985e7f3498ac66f&ver=1&model=M7&andorid=7.1.1'
    r = requests.get(url)
    result = r.json()
    if result['data']['list']:
        l1 = result['data']['list']
        count_dict_keys = count_dict.keys()
        for i in l1:
            if i['title'] not in count_dict_keys:
                count_dict[i['title']] = 1
            else:
                count_dict[i['title']] += 1

if __name__ == '__main__':
    for i in range(100):
        get_video()
    for i, j in count_dict.items():
        if j > 1:
            print('%s:%s' % (i, str(j)))
    print('count:', count_dict.__len__())

