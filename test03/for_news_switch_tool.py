from test03 import base_tools
import requests
def get_news_switch(url, parmes_dict):
    keys_li = ["api_key", 'imei', 'model', 'cs', 'app_ver']
    parmes_dict['api_sign'] = base_tools.get_request_api_sign(parmes_dict, keys_li)
    r = requests.get(url, params=parmes_dict)
    return r.json()['data']

if __name__ == '__main__':
    parmes_dict = {'api_key': '9dac6633be895da152187b9c1a5c0042',
                   'imei': '008600211651046',
                   'cs': '',
                   'app_ver': '1',
                   'model': 'M8'}
    hot_news_switch = get_news_switch('http://t-osapi-3g.gionee.com/api/news_switch/hotNews', parmes_dict)
    out_news_switch = get_news_switch('http://t-osapi-3g.gionee.com/api/news_switch/exitNews', parmes_dict)
    print('hot_news_switch:', hot_news_switch)
    print('out_news_switch:', out_news_switch)