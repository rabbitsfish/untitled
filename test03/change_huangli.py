import requests
from test03 import base_tools
result_dict = {}
parme = {
    'api_key' : '9dac6633be895da152187b9c1a5c0042',
    'model' : 'M7',
    'app_ver' : '5.3.3',
    'pkg' : 'com.android.calendar',
}
base_imei =  '0086002116510'
for i in range(100):
    if i < 10:
        imei = base_imei + '0' + str(i)
    else:
        imei = base_imei + str(i)
    parme['imei'] = imei
    parme['city'] = '深圳'
    parme_key = ["api_key", 'imei', 'model', 'app_ver',  'pkg']
    api_sign = base_tools.get_request_api_sign(parme, parme_key)
    parme['api_sign'] = api_sign
    r = requests.get('http://t-osapi-3g.gionee.com/api/volume_calendar/conf', params=parme)
    result = r.json()
    channel = result['data']['obj']['channel']
    if channel in result_dict.keys():
        result_dict[channel] = result_dict[channel] + 1
    else:
        result_dict[channel] = 1
print(result_dict)