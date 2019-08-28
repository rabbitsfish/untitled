import requests
count_list = {}
count_no_ad = 0
count_news_fail = 0
count_ad = 0
count_per_list = {}

def get_request(request_url):
    # print('request_url:', request_url)
    url = request_url.split('?')[0]
    par_url = request_url.split('?')[1]
    pars = par_url.split('&')
    data = {}
    for ele in pars:
        li = ele.split('=')
        data[li[0]] = li[1]
    # print(data)
    r = requests.get(url, params=data)
    result = r.json()
    return result

def get_show_count(request_url):
    '''

    :return: 发出获取资讯流以及广告的请求后，对所有的广告的曝光进行点击并统计广告类型的次数
    '''
    # request_url = 'http://t-osapi-3g.gionee.com/api/news_list/more?__debug=zhi-pu__debug' \
    #               '&sysvs=5.0.16&operators=&imei=008600214984988&app_ver=5.5.3&nettype=1' \
    #               '&ver=1&andorid=6.0&model=F5&lon=114.030832&client_id=CsY7aVd8JWaW0OUlo5RZqw%3D%3D&dpi=320' \
    #               '&carrier=0&coordinate_type=1&city=unknown&api_key=9dac6633be895da152187b9c1a5c0042' \
    #               '&connect_type=2&recoid=&apilevel=23' \
    #               '&app_list=com.qiyi.video%2Ccom.sankuai.meituan%2Ccom.zdanjian.zdanjian%2Ccom.dianping.v1%2Ccom.gionee.change.engine.vlife%2Ccom.tencent.mm%2Ccom.ssui.appmarket%2Ccom.baidu.searchbox%2Ccom.hzxwkj.myshare.sdk%2Ccom.tencent.qqpimsecure%2Ccom.tencent.qqlive%2Ccom.tencent.mtt%2Ccom.ss.android.article.news%2Ccom.meelive.ingkee%2Ccom.android.browser.test%2Ccom.jd.jrapp%2Ccom.tencent.news%2Ccom.jingdong.app.mall%2Ccom.autonavi.minimap%2Ccom.gionee.agileapp%2Ccom.baidu.haokan' \
    #               '&gps=114.030832%2522.542249&bss_id=34%3A12%3Af9%3A88%3Aee%3A48&del_app=&adver=2.0.1.dk' \
    #               '&mcc=460&apn=wifi&type=60&android_id=435622e138f20315&number=5&mac=b8%3A98%3Af7%3A05%3A8a%3A17&refreshtype=launch' \
    #               '&adslot_w=0&api_sign=83980603d2c8140b6b98b2029cc4cbc8&h=1280&w=720&package_name=com.android.browser&ftime=0&openudid=435622e138f20315' \
    #               '&cuid=DC0C042E4E4277D2F45D47C218695007&device_id=nQ7DOyvL3eRy8Ps1P7d2ndjexPsQQnZaMytbQw8%2BcII%3D' \
    #               '&ua=Mozilla_5_0__Linux__U__Android_6_0__zh_cn__Build_MRA58K___AppleWebKit_534_30__KHTML_like_Gecko__Version_4_0_Chrome_50_0_0_0_Mobile_Safari_534_30_GIONEE_F5_F5_RV_5_0_16' \
    #               '&ip=192.168.101.239&adslot_h=0&os_version=6.0&lat=22.542249&lac=1'
    result = get_request(request_url)
    # print('result:', result)
    li = result['data']['list']
    if (li != ''):
        for ele in li:
            # print('ele:', ele)
            if ele['ad_type'] == 1:
                global count_ad
                count_ad += 1
                if click_show_url(ele['selfshow'][0])['success']:
                    if ele['id'] in count_list.keys():
                        count_list[ele['id']] = count_list[ele['id']] + 1
                    else:
                        count_list[ele['id']] = 1
                break
            else:
                global count_no_ad
                count_no_ad = count_no_ad + 1
    else:
        global count_news_fail
        count_news_fail = count_news_fail + 1
    # print('count_list', count_list)



def get_config():
    '''

    :return: 获取广告配置
    '''
    request_url = 'http://t-osapi-3g.gionee.com/api/news_list/testGetConfig?module=SELF_INFO_AD&pkg=info.self.sdk.ads&imei=123455'
    result = get_request(request_url)
    return result

def click_show_url(show_url):
    '''

    :param show_url: 曝光链接
    :return: 点击曝光链接，获取response
    '''
    result = get_request(show_url)
    return result

def exchange_count():
    # get_show_count(request_url)
    # print('count_list:', count_list)
    # print('count_no_ad', count_no_ad)
    # print('count_news_fail', count_news_fail)
    # print('count_ad', count_ad)
    for id in count_list.keys():
        count_per_list[id] = count_list[id] / count_ad
    return count_per_list


if __name__ == '__main__':
    # for i in range(100):
    #     get_show_count()
    # print('count_list:', count_list)
    # print('count_no_ad', count_no_ad)
    # print('count_ad_fail', count_ad_fail)
    # print('count_ad', count_ad)
    # print(exchange_count())
    url = 'http://3gosapi.3gtest2.gionee.com/api/news_list/more?sdk=LIULANQI&client_id=Q4oZsgSvXyqLx3XA10Aflw==&dpi=480&carrier=0&timestamp=1565257760678&api_key=9dac6633be895da152187b9c1a5c0042&third_ad_support=1&ma=6666851257A2CCFC4A2B674AB25D895CCC7252D41F592B31E8ABA270C59F1199&connect_type=wifi&imei=57D463AE38317BA1A5571185291E3FC3&bss_id=34:12:f9:88:ee:44&mcc=460&apn=wifi&type=60&pkg=com.android.browser&android_id=c24180fde8209488&number=11&dw=1B5F7C84ADB1EA147780BAED5D6CCE96081F6BEEF997BD70B2E6A1CD6011F09B&app_ver=5.5.6.ar&refreshtype=pull_down&api_sign=6c68f637ba1df5c25d364c6d05adb5c8&h=1920&w=1080&openudid=c24180fde8209488&device_id=J6LGY5MsiXxmX+BoBvePe9lLbJC539nkbrbbICR7o6M=&cp_id=2&sdk_version=1.0.4.b&ua=Mozilla_5_0__Linux__U__Android_6_0__zh_cn__Build_MRA58K___AppleWebKit_534_30__KHTML_like_Gecko__Version_4_0_Chrome_50_0_0_0_Mobile_Safari_534_30_GIONEE_GN8002_GN8002_RV_5_0_16_GNBR_5_4_0_betas_Id_74FF923479FF242F0B7E76D152A11EC9&os_version=7.0&model=GIONEES10&lac=30516'
    # result = requests.get(url=url).text
    # print(result)
    for i in range(200):
        get_show_count(url)
    print('count_list:', count_list)
    print(exchange_count())
    # print(exchange_count(url))