import unittest.test
from test03 import for_news_switch_tool
class NewsSwitchCase(unittest.TestCase):
    parmes_dict = {'api_key': '9dac6633be895da152187b9c1a5c0042',
                   'imei': '008600211651046',
                   'cs': '',
                   'app_ver': '1',
                   'model': 'M8'}

    url = 'http://t-osapi-3g.gionee.com/api/news_switch/hotNews'
    def test_no_app_ver(self):
        '''版本号为空'''
        self.parmes_dict['app_ver'] = ''
        self.parmes_dict['cs'] = '6291CF4CB91BA6A334E4E7420791F862'  # 深圳
        result = for_news_switch_tool.get_news_switch(self.url, self.parmes_dict)
        self.assertEqual(result['obj']['main_switch'], 0, '开关为开')
        self.assertEqual(result['msg'], 'blocked by enable app ver', '版本号被限制')

    def test_limit_app_ver(self):
        '版本号被限制'
        self.parmes_dict['app_ver'] = '1'
        self.parmes_dict['cs'] = '6291CF4CB91BA6A334E4E7420791F862'  # 深圳
        result = for_news_switch_tool.get_news_switch(self.url, self.parmes_dict)
        self.assertEqual(result['obj']['main_switch'], 0, '开关为开')
        self.assertEqual(result['msg'], 'blocked by enable app ver', '版本号被限制')

    def test_success_app_ver(self):
        '''限制内的版本号'''
        self.parmes_dict['app_ver'] = '5.0.6'
        self.parmes_dict['cs'] = '6291CF4CB91BA6A334E4E7420791F862'  #深圳
        result = for_news_switch_tool.get_news_switch(self.url, self.parmes_dict)
        self.assertEqual(result['obj']['main_switch'], 1, '开关为关')

    def test_no_city(self):
        '城市为空'
        self.parmes_dict['app_ver'] = '5.0.6'
        self.parmes_dict['cs'] = ''
        result = for_news_switch_tool.get_news_switch(self.url, self.parmes_dict)


