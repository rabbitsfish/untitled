import requests

url = 'https://dsp-api.zhongxunrunda.com/dsp/mobi/landingPage?redirect=ED18BEFD63255A1974D63BDB556004E0&reqId=18b619c9-7a66-44c0-9062-1adfed3d4078&adToken=75a0414fc6224bcca29204b464e15f54'
r = requests.get(url)
print(r.content)
