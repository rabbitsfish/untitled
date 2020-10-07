# import sys
# import os
# base_tools_path = os.path.abspath('C:\\Users\\dongff\\PycharmProjects\\untitled\\test03\\base_tools')
# curPath = os.path.abspath(os.path.dirname(base_tools_path))
# sys.path.append(curPath)
# print(sys.path)
# from test03 import base_tools
import requests

def encryption_s(s):
    url = 'http://t-osapi-3g.gionee.com/api/adminapi/imei?type=encode&imei=%s' % s
    r = requests.get(url)
    # print(r.text)
    return r.text

def get_imeis():
    base_imei='00860021165104'
    imei_list = []
    for i in range(10):
        imei = base_imei + str(i)
        imei_list.append({'imei_name' : encryption_s(imei)})
    print('imei_list:', imei_list)
    return imei_list

def replace_to_blank(model_name):
    if '%20' in model_name:
        model_name.replace('%20', ' ')
    return model_name

def get_result(content_data, result_bol):
    print('result_bol:', result_bol)
    flag = 'adRatio' in content_data.keys()
    assert  flag == result_bol


def get_result_bol(imei_name, model_name):
    if imei_name in ['008600211651001', '008600211651002'] and model_name in ['GIONEE M7', 'GIONEE M6']:
        return True
    else:
        return False

def get_adaptOtherMusicSwitch_config(imei_name):
    if imei_name.endswith(('0', '1', '2', '3')):
        return True
    else:
        return False

def get_adaptOtherMusicSwitch_result(content, result_bol):
    result = 'adaptOtherMusicSwitch' in content.keys()
    assert result == result_bol


def get_testX1_config(imei_name, model_name):
    if imei_name.endswith(('0', '1', '2')) and model_name in ('M7'):
        return 'false'
    else:
        return 'true'


def get_testX2_config(imei_name, model_name):
    if imei_name.endswith(('0', '1', '2')) and model_name not in ('GIONEE M7'):
        return 'false'
    else:
        return 'true'


# if __name__ == '__main__':
#     print(111)