import requests
from test03 import base_tools

parm_str = 'sdk=LIULANQI&client_id=lUHgA5t4xoIHtOm8CHsltg==&dpi=320&carrier=0&timestamp=1564494378440&api_key=9dac6633be895da152187b9c1a5c0042&third_ad_support=1&ma=A57EF08875918B99E37936F1A9D587D39CA75ACA85544EF1C4A0C6E58BADDEB2&connect_type=wifi&imei=EC0CC6C3767A25177A0AB9CD0F4255C7&bss_id=34:12:f9:88:ee:44&mcc=460&apn=wifi&type=60&pkg=com.android.browser&android_id=2b38ae6cb26d2a09&number=11&dw=A0CE83816089DDD4709FFAF9AF62C6F0&app_ver=5.5.6.an&refreshtype=pull_down&api_sign=aab31216ebe878a5b31362f6af7b9f89&h=1280&w=720&openudid=2b38ae6cb26d2a09&device_id=itd0AmRmQ7N0dvB36d68WnmUjFG8rksdPjeU/6jaBIU=&cp_id=8&sdk_version=1.0.3.m&ua=Mozilla_5_0__Linux__U__Android_6_0__zh_cn__Build_MRA58K___AppleWebKit_534_30__KHTML_like_Gecko__Version_4_0_Chrome_50_0_0_0_Mobile_Safari_534_30_GIONEE_GN8002_GN8002_RV_5_0_16_GNBR_5_4_0_betas_Id_74FF923479FF242F0B7E76D152A11EC9&os_version=5.1&lac=1&model=GN3001'

def get_news_and_ad(imei, result_count, keys_normal_li):
    url = 'http://3gosapi.3gtest2.gionee.com/api/news_list/more'
    parm_str = 'sdk=LIULANQI&client_id=lUHgA5t4xoIHtOm8CHsltg==&dpi=320&carrier=0&timestamp=1564494378440&api_key=9dac6633be895da152187b9c1a5c0042&third_ad_support=1&ma=A57EF08875918B99E37936F1A9D587D39CA75ACA85544EF1C4A0C6E58BADDEB2&connect_type=wifi&imei=EC0CC6C3767A25177A0AB9CD0F4255C7&bss_id=34:12:f9:88:ee:44&mcc=460&apn=wifi&type=60&pkg=com.android.browser&android_id=2b38ae6cb26d2a09&number=11&dw=A0CE83816089DDD4709FFAF9AF62C6F0&app_ver=5.5.6.an&refreshtype=pull_down&api_sign=aab31216ebe878a5b31362f6af7b9f89&h=1280&w=720&openudid=2b38ae6cb26d2a09&device_id=itd0AmRmQ7N0dvB36d68WnmUjFG8rksdPjeU/6jaBIU=&cp_id=8&sdk_version=1.0.3.m&ua=Mozilla_5_0__Linux__U__Android_6_0__zh_cn__Build_MRA58K___AppleWebKit_534_30__KHTML_like_Gecko__Version_4_0_Chrome_50_0_0_0_Mobile_Safari_534_30_GIONEE_GN8002_GN8002_RV_5_0_16_GNBR_5_4_0_betas_Id_74FF923479FF242F0B7E76D152A11EC9&os_version=5.1&lac=1&model=GN3001'
    parm_dict = base_tools.get_request_parmes(parm_str)
    # base_imei = '00860021165101'
    # parm_dict['imei'] = imei
    parm_dict['api_sign'] = base_tools.get_request_api_sign(parm_dict, keys_normal_li)
    r = requests.get(url, params=parm_dict)
    # print(r.json())
    li = r.json()['data']['list']
    for ele in li:
        if 'id' in ele.keys():
            if ele['id'] in result_count.keys():
                result_count[ele['id']] += 1
            else:
                result_count[ele['id']] = 1
            break

# def get_diff_parm(keys_normal_li, parm_dict):
#     for key in keys_normal_li:
#         if key not in list(parm_dict.keys()):
#             print('key:', key)
#     print('keys_normal_li:', keys_normal_li.__len__())
#     print('parm_dict:', parm_dict.__len__())

if __name__ == '__main__':
    result_count = {}
    # keys_normal_li = ['api_key' ,'cp_id', 'pkg', 'cs', 'dw', 'dw_type', 'mc', 'ma', 'app_ver', 'model', 'api_key', 'api_sign', 'type', 'imei', 'number', 'apn', 'openudid', 'ua', 'os_version', 'android_id', 'w', 'h', 'dpi', 'ip', 'connect_type', 'carrier', 'lac', 'mcc', 'bss_id', 'client_id', 'device_id', 'refreshtype', 'timestamp', 'third_ad_support']
    keys_normal_li = ['api_key', 'cp_id', 'pkg', 'cs', 'dw', 'app_ver', 'model', 'imei', 'type', 'number', 'refreshtype', 'timestamp', 'carrier', 'connect_type', 'openudid', 'sdk_version', 'sdk']
    base_imei = '00860021165101'
    for i in range(10):
        imei = base_imei + str(i)
        get_news_and_ad(imei, result_count, keys_normal_li)
    print(result_count)