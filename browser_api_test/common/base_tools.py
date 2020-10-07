import hashlib
import requests
def get_request_parmes(parmes):
    parme_list = parmes.split('&')
    parme_dict = {}
    for parme in parme_list:
        parme_per = parme.split('=')
        parme_dict[parme_per[0]] = parme_per[1]
    # print(parme_dict)
    return parme_dict

def get_request_api_sign(parme_dict, keys_normal_li):
    encryption_parme(parme_dict, 'cs', 'imei', 'city')
    # print('parme_dict__:', parme_dict)
    api_keys_dict = {
        'cb412e048ee48f5f6ca62f9bf339a069' : '84ccd57681cea4ae9ccac0517fd2e0dd',
        '9dac6633be895da152187b9c1a5c0042' : '587ca62428fbb663bb652a49d88bf7e7',
    }
    # keys_normal_li = ['api_key', 'imei' , 'model' , 'city' , 'app_ver' , 'sdk_ver', 'version', 'sysvs',  'nettype',  'ver',  'andorid']
    keys_li = []
    parme_values = ''
    for key in parme_dict.keys():
        if key in keys_normal_li:
            keys_li.append(key)
    if keys_li.__len__() > 0:
        keys_li.sort()
    for key in keys_li:
        parme_values = parme_values + parme_dict[key]
    parme_values = parme_values + api_keys_dict[parme_dict['api_key']]
    # print('parme_values:', parme_values)
    api_sign = get_values_MD5(parme_values)
    # print('api_sign:', api_sign)
    return api_sign

def get_values_MD5(values_string):
    m2 = hashlib.md5()
    m2.update(values_string.encode('utf-8'))
    return m2.hexdigest()

def encryption_parme(parme_dict, *args):
    for en_key in args:
        if en_key in parme_dict.keys():
            parme_dict[en_key] = encryption_s(parme_dict[en_key])
    # return parme_dict

def encryption_s(s):
    url = 'http://t-osapi-3g.gionee.com/api/adminapi/imei?type=encode&imei=%s' % s
    r = requests.get(url)
    # print(r.text)
    return r.text


if __name__ == '__main__':
    # pass
    get_request_api_sign(get_request_parmes('sysvs=5.1.16&operators=&imei=61374BE70391D138C59679F7928FD8C9&app_ver=5.5.6&nettype=1&sdk_support=1&third_ad_support=2&ver=1&model=M7&andorid=7.1.1&city=上海'))
    # get_request_parmes(
    #     'sysvs=5.1.16&imei=008600211651046&app_ver=5.5.6&version=1564390229&nettype=4&api_key=9dac6633be895da152187b9c1a5c0042&api_sign=a74263c203dfb7c7b7632b38623b7d0c&sdk_ver=1.0&model=M7&andorid=25')
    keys_normal_li = ['imei' , 'model' , 'city' , 'app_ver' , 'version']
    result = get_request_api_sign(get_request_parmes('sysvs=5.1.16&operators=&imei=865843024870690&app_ver=5.5.6&nettype=1&third_ad_support=1&ver=1&model=F205&andorid=7.1.1&api_key=9dac6633be895da152187b9c1a5c0042&city=深圳'), keys_normal_li=keys_normal_li)
    print(result)
    print(get_values_MD5('008600211651046'))
