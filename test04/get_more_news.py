import requests
def get_more_news():
    url = 'http://t-osapi-3g.gionee.com/api/news_hot/more'
    parmes = 'app_ver=5.5.6&mac=B8:98:F7:D4:E0:B4&api_key=9dac6633be895da152187b9c1a5c0042&api_sign=9266a16bfeb23489110d5371788f5357&dtype=exitNewsWindow&h=2016&cs=&w=1080&openudid=4c84d6633b6eb712&imei=008600211651046&ua=Mozilla%2F5.0%20%28Linux%3B%20Android%207.1.1%3B%20GIONEE%20M7%20Build%2FN6F26Q%3B%20wv%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Version%2F4.0%20Chrome%2F58.0.3029.83%20Mobile%20Safari%2F537.36&nettype=1&os_version=5.1.16&model=M7&android_id=4c84d6633b6eb712'
    parmes_list = parmes.split('&')
    parmes_dict = {}
    result_list = {}
    before_result = {}
    for i in parmes_list:
        p = i.split('=')
        parmes_dict[p[0]] = p[1]
    for i in range(60):
        result = requests.post(url, data=parmes_dict).json()
        # if before_result == {}:
        #     before_result = result['data']
        # else:

        for ele in result['data']:
            if ele['id'] in result_list.keys():
                result_list[ele['id']] = result_list[ele['id']] + 1
            else:
                result_list[ele['id']] = 1
    for i, j in result_list.items():
        if j > 1:
            print('非正常得：%s:%d' % (i, j))
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        else:
            print('正常得：%s:%d' % (i, j))
    print(result_list.__len__())

if __name__ == '__main__':
    get_more_news()

