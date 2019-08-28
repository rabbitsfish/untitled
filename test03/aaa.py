import requests
url1 = 'http://t-3g.gionee.com//api/lock_screen/information_ql'
url2 = 'http://3g.3gtest2.gionee.com/api/lock_screen/charging'
imei_base = '0086002116510'
count_true = 0
count_false  = 0
for i in range(100):
    if i < 10:
        imei = imei_base + '0' + str(i)
    else:
        imei = imei_base + str(i)
    data1 = {
        'imei' : imei
    }
    data2 = {
        'sysvs' : '5.1.16',
        'operators' : '',
        'imei' : imei,
        'app_ver' : '5.5.5',
        'nettype' : '1',
        'ver' : '1',
        'model' : 'M7',
        'andorid': '7.1.1',
        '__debug': 'zhi-pu__debug',
    }
    r1 = requests.get(url1, params=data1)
    response_url1 = r1.json()['data']['url']
    print("response_url1:",response_url1 )
    r2 = requests.get(url2, params=data2)
    response_url2 = r2.json()["data"]['obj']["information_url"]
    if response_url1 == response_url2:
        print(imei, ":Yes")
        count_true = count_true + 1
    else:
        count_false = count_false + 1

print('count_true:', count_true)
print('count_false', count_false)