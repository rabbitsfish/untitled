# import redis
# port = 6379
# ip = '127.0.0.1'
# r = redis.Redis(host=ip, port=port, decode_responses=True)
# pool = redis.ConnectionPool(host=ip, port=port)
# r1 = redis.Redis(connection_pool=pool, decode_responses=True)
# r.set('name', 'Lily')
# r1.set('foo', 'bar')
# print(r1.get('foo'))
# print(r.get('name'))
import requests
data = {'api_key': '9dac6633be895da152187b9c1a5c0042',
        'imei' : '865843024870690',
        'app_ver' : '5.5.6',
        'model' : 'F205',
        'city' : '深圳'
        }
for i in range(10):
    r = requests.get('http://3g.3gtest2.gionee.com/api/lock_screen/charging?sysvs=5.1.16&operators=&'
                     'imei=865843024870690&app_ver=5.5.6&nettype=1&third_ad_support=1&ver=1&model=F205&andorid=7.1.1&'
                     'api_key=9dac6633be895da152187b9c1a5c0042&city=深圳')
    r.encoding = 'utf-8'
    print(r.json())