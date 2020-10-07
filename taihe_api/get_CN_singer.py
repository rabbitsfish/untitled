import requests
import json
url = 'http://dl-music.3gtest2.gionee.com/api/artist/hotList?region=CN&gender=&page=-1&pageSize=-1&api_sign=a6f6217bf074d622969af54a70ef286d&api_key=2e69439ca6c628c7fba819c3005fa96a&userId=0293C10C9F123F29B3C200318F091C1D&model=GIONEE%20M7&appVer=5.3.6.c&verCode=2026536002'
data =  {
    "app": {
        "appName": "音乐",
        "packageName": "com.android.music",
        "versionCode": 2026536002,
        "versionName": "5.3.6.c"
    },
    "device": {
        "androidId": "89d6eb22d500bd96",
        "brand": "GIONEE",
        "dip": 480,
        "imei": "0293C10C9F123F29B3C200318F091C1D",
        "imsi": "68821B608D82405389B8DCB6018E9A54",
        "mac": "3F0D344E9CDE036D655825E04C297C8E6BF87A6E0F860CAE0CDDE18F158B44F4",
        "manufacturer": "GIONEE",
        "model": "GIONEE M7",
        "orientation": 0,
        "os": "Android",
        "osLevel": 25,
        "osVersion": "7.1.1",
        "screenHeight": 2160,
        "screenWidth": 1080,
        "serialno": "0293C10C9F123F29B3C200318F091C1D",
        "ua": "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn;GIONEE-GIONEE M7/Phone Build/IMM76D) AppleWebKit534.30(KHTML,like Gecko)Version/4.0 Mobile Safari/534.30 Id/0293C10C9F123F29B3C200318F091C1D RV/7.1.1",
        "vendor": "GIONEE"
    },
    "network": {
        "carrier": 0,
        "cellularId": 54318735,
        "connectType": "NETWORK_WIFI",
        "ipv4": "192.168.101.34"
    },
    "timestamp": 1579248882301
}
result = requests.post(url, json=data)
print(result.text)