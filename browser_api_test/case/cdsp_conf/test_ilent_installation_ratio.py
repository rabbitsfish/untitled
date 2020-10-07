import unittest
import requests
from test03 import base_tools
class TEstIlentInstallationRation(unittest.TestCase):
    '''充电锁屏的静默安装比例验证'''

    @classmethod
    def setUpClass(cls):
        # cls.url = 'http://t-3g.gionee.com/api/switch_a/silence'
        cls.url = 'http://3g.gionee.com/api/switch_a/silence'
        cls.arr_sign = ["api_key", 'imei', 'model', 'city', 'sdk', 'from']
        cls.data = {
            'imei': '008600211651046',
            'model': 'M7',
            'api_key': '9dac6633be895da152187b9c1a5c0042',
        }

    def test_ration(self):
        '''测试充电锁屏的比例'''
        result_li = {1: 0, 0: 0}
        self.data['city'] = '深圳'
        self.data['sdk'] = 'toutiao_SDK'
        self.data['from'] = 'cdsp'
        self.data['api_sign'] = base_tools.get_request_api_sign(self.data, self.arr_sign)
        percent = requests.get(self.url, params=self.data).json()['data']['obj']['chance']
        for i in range(100):
            r = requests.get(self.url, params=self.data)
            result = r.json()
            result_li[result['data']['obj']['silence']] += 1
        print(result_li)
        self.assertEqual(result_li[1] + result_li[0], 100)
        self.assertLessEqual(percent, result_li[1] + 10)
        self.assertLessEqual(result_li[1] - 10, percent)
        self.assertLessEqual(100 - percent, result_li[0] + 10)
        self.assertLessEqual(result_li[0] - 10, 100 - percent)

    if __name__ == '__main__':
        unittest.main()