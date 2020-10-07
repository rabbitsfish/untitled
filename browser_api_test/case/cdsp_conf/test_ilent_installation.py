import unittest
import requests
from browser_api_test.common import base_tools
class TestSilentInstallation(unittest.TestCase):
    '''充电锁屏的静默安装验证'''
    @classmethod
    def setUpClass(cls):
        cls.url = 'http://t-3g.gionee.com/api/switch_a/silence'
        cls.arr_sign = ["api_key" , 'imei' , 'model' , 'city' , 'sdk', 'from']
        cls.data = {
            'imei': '008600211651046',
            'model': 'M7',
            'api_key': '9dac6633be895da152187b9c1a5c0042',
        }

    def test_contain_sdk_and_cdsp(self):
        '''SDK为头条，来源为充电锁屏   配置比例100%，不验证比例，只验证结果'''
        self.data['city'] = '深圳'
        self.data['sdk'] = 'toutiao_SDK'
        self.data['from'] = 'cdsp'
        self.data['api_sign'] = base_tools.get_request_api_sign(self.data, self.arr_sign)
        print(self.data['api_sign'])
        r = requests.get(self.url, params=self.data)
        result = r.json()
        # print(r.json())
        self.assertEqual(result['msg'], 'success')
        self.assertEqual(result['data']['obj']['silence'], 1)

    def test_contain_no_sdk_and_cdsp(self):
        '''SDK为非头条，来源为充电锁屏'''
        self.data['city'] = '深圳'
        self.data['sdk'] = 'notoutiao_SDK'
        self.data['from'] = 'cdsp'
        self.data['api_sign'] = base_tools.get_request_api_sign(self.data, self.arr_sign)
        r = requests.get(self.url, params=self.data)
        result = r.json()
        print(result)
        self.assertEqual(result['msg'], 'success')
        self.assertEqual(result['data']['obj']['silence'], 0)

    def test_contain_sdk_and_no_cdsp(self):
        'SDK为头条，来源为非充电锁屏'
        self.data['city'] = '深圳'
        self.data['sdk'] = 'toutiao_SDK'
        self.data['from'] = 'nocdsp'
        self.data['api_sign'] = base_tools.get_request_api_sign(self.data, self.arr_sign)
        r = requests.get(self.url, params=self.data)
        result = r.json()
        print(result)
        self.assertEqual(result['msg'], 'success')
        self.assertEqual(result['data']['obj']['silence'], 1)

    def test_contain_no_sdk_and_no_cdsp(self):
        self.data['city'] = '深圳'
        self.data['sdk'] = 'notoutiao_SDK'
        self.data['from'] = 'nocdsp'
        self.data['api_sign'] = base_tools.get_request_api_sign(self.data, self.arr_sign)
        r = requests.get(self.url, params=self.data)
        result = r.json()
        print(result)
        self.assertEqual(result['msg'], 'success')
        self.assertEqual(result['data']['obj']['silence'], 0)

if __name__ == '__main__':
    unittest.main()