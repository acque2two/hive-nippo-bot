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

a="Testsssss"
b="で"
c="やって"
d="みました"

HITOKOTO_TODAY = a
LEARNED_TODAY = b
TODO_TOMORROW = c
TASK_NEXT_CLASS =d

params = {'token':'xoxp-8534391651-219333654307-280723382546-bcd2278e3dd44dffd57dcbd2ddf16e29',
         'channel': channel['id'],
         'text': '''

[今日のひとこと]
 %s
[本日学んだこと]
%s
[明日行うこと]
 %s
 [次回までの課題]
%s
          ''' %(HITOKOTO_TODAY, LEARNED_TODAY, TODO_TOMORROW, TASK_NEXT_CLASS)}


start_time=datetime.time(13,29,0)
while now<start_time:
    time.sleep(1)
    now=datetime.datetime.now().time()
res = requests.post( url, params=params)
print(res)
