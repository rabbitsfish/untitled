import requests
# url = 'http://t-music-search.banqumusic.com/search/words/merge'
# data = {
# 	"timestamp": 1594438030239,
# 	"word": "王菲",
# 	"type": "15",
# 	"page": "1",
# 	"pageSize": "5",
# 	"brand": "meizu",
# 	"imei": "866309040108100",
# 	"model": "Note9",
# 	"appVer": "9.1.9",
# 	"appId": "2e69439ca6c628c7fba819c3005fa96a",
# 	"verCode": "9001009",
# 	"osVer": "28",
# 	"netType": "NETWORK_WIFI",
# 	"mac": "86F32AD633AB6A4CF55F78F91AA8FA80574DE21147733E5BF95C043F567C0503",
# 	"data": {
# 		"word": "王菲",
# 		"type": "15"
# 	}
# }
# header = {
#     'Content-type': 'application/json;charset=UTF-8'
# }
# r = requests.post(url=url, json=data, headers=header)
# result = r.json()
# print(result)
# print(r.headers)

import binascii
def hexStr_to_str(hex_str):
	#hex_str = '7b226370223a224154222c2263704964223a223130313037303139222c22736f6e674964223a223233323839313338227d'
	hex = binascii.a2b_hex(hex_str)
	return hex

data = {
	"timestamp": 1594808512448,
	"requestId": "7aa9759cda6e4632bcf927b7786f260d",
	"brand": "meizu",
	"imei": "86630904010810",
	"model": "Note9",
	"appVer": "1.0.1",
	"appId": "2e69439ca6c628c7fba819c3005fa96a",
	"verCode": "1000001",
	"osVer": "28",
	"netType": "NETWORK_WIFI",
	"mac": "86F32AD633AB6A4CF55F78F91AA8FA80574DE21147733E5BF95C043F567C0503",
	"data": {
		"list": [],
		"token": "6b84859c1b70abeddbfb6e32eeed68912d0818f423421c74c61ab0de866ba9d2"
	}
}
url = 'http://t-music-api.banqumusic.com/api/recommend/song/day/recommendSongList?signature=8932424185c731d40a6f2979d32ef87d&output=json&appId=2e69439ca6c628c7fba819c3005fa96a'
r = requests.post(url=url, json=data)
result = r.json()
li = result['data']['list']
cp_result = {'TH': 0, 'AT': 0, 'other': 0}
for i in range(len(li)):
	songId = li[i]['songId']
	songId_hex = hexStr_to_str(songId)
	print('songId_hex:', songId_hex)
	songId_cp = eval(songId_hex)['cp']
	if songId_cp == 'TH':
		cp_result['TH'] = cp_result['TH'] + 1
	elif songId_cp == 'AT':
		cp_result['AT'] = cp_result['AT'] + 1
	else:
		cp_result['other'] = cp_result['other'] + 1
print(cp_result)
