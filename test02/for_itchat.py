import itchat.content
import requests
import time

RECEIVE_MSG = ''
def get_tuling_text():
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": RECEIVE_MSG
            },
        },
        "userInfo": {
            "apiKey": "40530c20e6e842d1a1d6a8d2e4f69610",
            "userId": "tulingbaobaotulingbaobaotulingba"
        }
    }
    headers = {
        'Content-Type': 'application/json',
    }
    r = requests.post(url, json=data, headers=headers)
    reply_msg_text = r.json()['results'][0]['values']['text']
    print('response:',reply_msg_text)
    return reply_msg_text

# @itchat.msg_register(itchat.content.TEXT)
# def reply_msg(msg):
#     global RECEIVE_MSG
#     RECEIVE_MSG = msg.text
#     print("收到一条信息：", msg.text)

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    global RECEIVE_MSG
    RECEIVE_MSG = msg.text
    print('RECEIVE_MSG:', RECEIVE_MSG)
    reply_msg_text = get_tuling_text()
    itchat.send('%s' % reply_msg_text, msg['FromUserName'])

if __name__ == '__main__':
    itchat.auto_login()
    time.sleep(5)
    #itchat.send("文件助手你好哦", toUserName="filehelper")
    itchat.run()