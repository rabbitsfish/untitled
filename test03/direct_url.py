import requests
url = 'http://admin.3g.3gtest2.gionee.com/Admin/Login/login'
host = 'http://admin.3g.3gtest2.gionee.com'
data = {
    'username' : 'admin',
    'password' : 'dongliang2019',
}
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    # 'Cookie' : 'PHPSESSID=ein50ibcg27h4tf2nv5llu0ee7; _securityCode=2407923491',
    # 'Refere' : 'http://admin.3g.3gtest2.gionee.com/Admin/Login/index',
}

result = requests.post(url, data=data, headers=headers, allow_redirects=False)
result.encoding = 'utf-8'
print(result.status_code)
print(result.text)
cookie_result = result.headers['Set-Cookie']
location_result = result.headers['Location']
headers['Cookie'] = cookie_result
result = requests.get('%s%s' % (host, location_result), headers=headers)
result.encoding = 'utf-8'
print(result.text)