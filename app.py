#coding: utf-8

import requests
import json
import datetime,time

url = "https://slack.com/api/channels.list"

params = {'token':'xoxp-8534391651-219333654307-280723382546-bcd2278e3dd44dffd57dcbd2ddf16e29'}
res = requests.post( url, params=params)

channels = json.loads(res.text)
channel = list(filter(lambda x: x['name_normalized'] == 'for_test_python', channels['channels']))[0]


url = "https://slack.com/api/chat.postMessage"

def hoge (fuga):
    
    text = "【今日やったこと】 \n"
    text += fuga[1] + "\n"
    text += "【今日学んだこと】 \n"
    text += fuga[2] + "\n"
    text += "【明日行うこと】 \n"
    text += fuga[3] + "\n"
    text += "【次回までの課題】 \n"
    text += fuga[4] + "\n"
    return text


params = {'token':'xoxp-8534391651-219333654307-280723382546-bcd2278e3dd44dffd57dcbd2ddf16e29',
         'channel': channel['id'],
         'text': hoge(mesgs)}


start_time=datetime.time(13,29,0)
while now<start_time:
    time.sleep(1)
    now=datetime.datetime.now().time()
res = requests.post( url, params=params)
print(res)
