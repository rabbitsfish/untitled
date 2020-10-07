# import requests
# from test03 import base_tools
# result_dict = {}
# parme = {
#     'api_key' : '9dac6633be895da152187b9c1a5c0042',
#     'model' : 'M7',
#     'app_ver' : '5.3.3',
#     'pkg' : 'com.android.music',
#     'release' : 'p'
# }
# base_imei =  '0086002116510'
# for i in range(100):
#     if i < 10:
#         imei = base_imei + '0' + str(i)
#     else:
#         imei = base_imei + str(i)
#     parme['imei'] = imei
#     parme['city'] = '深圳'
#     parme_key = ["api_key", 'imei', 'model', 'release',  'pkg']
#     api_sign = base_tools.get_request_api_sign(parme, parme_key)
#     parme['api_sign'] = api_sign
#     r = requests.get('http://t-osapi-3g.gionee.com/api/news_list/conf', params=parme)
#     result = r.json()
#     print(result)
#     channel = result['data']['obj']['channel']
#     if channel in result_dict.keys():
#         result_dict[channel] = result_dict[channel] + 1
#     else:
#         result_dict[channel] = 1
# print(result_dict)

s1 = 'http://3gosapi.3gtest2.gionee.com/api/news_list/more?sdk=MUSIC_HOME&client_id=/wOSq5iL7vCaKb+ATFhBWw==&dpi=480&carrier=0&timestamp=1573843955761&api_key=9dac6633be895da152187b9c1a5c0042&third_ad_support=2&ma=A2680AB1A08D4E26A078EA929972D53CAB8C39391C4B5FDC5E39EF1698CD48EB&connect_type=wifi&imei=61374BE70391D138C59679F7928FD8C9&bss_id=34:12:f9:88:ee:44&mcc=460&apn=wifi&type=183&pkg=com.android.music&android_id=4c84d6633b6eb712&number=11&dw=33A7D02791C673E4B12A4C748AD095BE&app_ver=5.3.3.f&refreshtype=channel&api_sign=414bbc4cd17226364138c5f42b2c663b&h=2016&w=1080&openudid=4c84d6633b6eb712&device_id=ySZ+dWe+v5MAAL9AzeBHuNinZb76QRZqg3nFJ+YjjU0=&cp_id=10&sdk_version=1.0.4.b&ua=Mozilla_5_0__Linux__U__Android_6_0__zh_cn__Build_MRA58K___AppleWebKit_534_30__KHTML_like_Gecko__Version_4_0_Chrome_50_0_0_0_Mobile_Safari_534_30_GIONEE_GN8002_GN8002_RV_5_0_16_GNBR_5_4_0_betas_Id_74FF923479FF242F0B7E76D152A11EC9&os_version=7.1.1&model=GIONEEM7&lac=1'
s2 = 'http://3gosapi.3gtest2.gionee.com/api/news_list/more?sdk=MUSIC_HOME&client_id=/wOSq5iL7vCaKb+ATFhBWw==&dpi=480&carrier=0&timestamp=1573843945505&api_key=9dac6633be895da152187b9c1a5c0042&third_ad_support=2&ma=A2680AB1A08D4E26A078EA929972D53CAB8C39391C4B5FDC5E39EF1698CD48EB&connect_type=wifi&imei=61374BE70391D138C59679F7928FD8C9&bss_id=34:12:f9:88:ee:44&mcc=460&apn=wifi&type=60&pkg=com.android.music&android_id=4c84d6633b6eb712&number=11&dw=33A7D02791C673E4B12A4C748AD095BE&app_ver=5.3.3.f&refreshtype=pull_down&api_sign=dd888cd62b3d18d4d5022a80bfc4a7c0&h=2016&w=1080&openudid=4c84d6633b6eb712&device_id=ySZ+dWe+v5MAAL9AzeBHuNinZb76QRZqg3nFJ+YjjU0=&cp_id=10&sdk_version=1.0.4.b&ua=Mozilla_5_0__Linux__U__Android_6_0__zh_cn__Build_MRA58K___AppleWebKit_534_30__KHTML_like_Gecko__Version_4_0_Chrome_50_0_0_0_Mobile_Safari_534_30_GIONEE_GN8002_GN8002_RV_5_0_16_GNBR_5_4_0_betas_Id_74FF923479FF242F0B7E76D152A11EC9&os_version=7.1.1&model=GIONEEM7&lac=1'