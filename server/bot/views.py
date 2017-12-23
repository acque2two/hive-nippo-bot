import requests

from django.shortcuts import render
from django.http import HttpResponse

from .load_serif import slack_serif

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = "scu5LBxiuOawhnK1iP6hQtmFd+CC/DHcqymtNx+vPjvLY5ktNbmGXn6xXqCrksbfOtwFktcjg4MLvUmb88DHXZccwfW9LdVosejRT+16AVja2i07HJfxk0RpjKVpSVFhulF5TT1tt1+uGnDAGFYpIgdB04t89/1O/w1cDnyilFU="
HEADER = {
    "Content-Type":  "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
}

import requests
import json
import datetime, time


def slack_send(mesg_dict):
    url = "https://slack.com/api/channels.list"

    params = {'token': 'xoxp-8534391651-219333654307-280723382546-bcd2278e3dd44dffd57dcbd2ddf16e29'}
    res = requests.post(url, params=params)

    channels = json.loads(res.text)
    channel = list(filter(lambda x: x['name_normalized'] == 'for_test_python', channels['channels']))[0]

    url = "https://slack.com/api/chat.postMessage"

    def hoge(fuga):
        text = "名前: " + fuga["name"] + "\n"
        text += "【今日やったこと】 \n"
        text += fuga["today_comment"] + "\n"
        text += "【今日学んだこと】 \n"
        text += fuga["today_studies"] + "\n"
        text += "【明日行うこと】 \n"
        text += fuga["tomorrow_do"] + "\n"
        text += "【次回までの課題】 \n"
        text += fuga["quest_for_next"] + "\n"
        return text

    params = {'token':          'xoxp-8534391651-219333654307-280723382546-bcd2278e3dd44dffd57dcbd2ddf16e29',
              'channel': channel['id'],
              'text':           hoge(mesg_dict)}

    # start_time=datetime.time(13,29,0)
    # while now<start_time:
    #     time.sleep(1)
    #     now=datetime.datetime.now().time()
    res = requests.post(url, params=params)
    print(res)


def index(request):
    return HttpResponse("This is bot api.")


# Create your views here.
import json


def reply_text(reply_token, text):
    # reply = komento =[[今日の一言], [本日学んだこと], [明日行うこと], [次回までの課題]]
    # for i in komento:

    payload = {
        "replyToken": reply_token,
        "messages":   [
            {
                "type": "text",
                "text": text
            }
        ]
    }
    requests.post(REPLY_ENDPOINT, headers=HEADER, data=json.dumps(payload))  # LINEにデータを送信
    return text


KIKUYATU_ITIRAN = [
    "名前を入力してください。",
    "「今日の一言」を入力してください。",
    "「本日学んだこと」を入力してください。",
    "「明日行うこと」を入力してください。",
    "「次回までの課題」を入力してください。"
]

user_saw = {}


def callback(request):
    reply = ""
    request_json = json.loads(request.body.decode('utf-8'))  # requestの情報をdict形式で取得
    for e in request_json['events']:
        reply_token = e['replyToken']  # 返信先トークンの取得
        message_type = e['message']['type']  # typeの取得

        if message_type == 'text':
            text = e['message']['text']  # 受信メッセージの取得
            if e['source']['userId'] not in user_saw:
                user_saw[e['source']['userId']] = {}

            if "name" not in user_saw[e['source']['userId']]:
                user_saw[e['source']['userId']]["name"] = ""  # 次に入力するものを空の文字列で示す
                reply_text(reply_token, KIKUYATU_ITIRAN[0])
            elif "today_comment" not in user_saw[e['source']['userId']]:
                user_saw[e['source']['userId']]["name"] = e['message']['text']  # 実際に文字を入力する
                user_saw[e['source']['userId']]["today_comment"] = ""  # 次に入力するものを空の文字列で示す
                reply_text(reply_token, KIKUYATU_ITIRAN[1])
            elif "today_studies" not in user_saw[e['source']['userId']]:
                user_saw[e['source']['userId']]["today_comment"] = e['message']['text']  # 実際に文字を入力する
                user_saw[e['source']['userId']]["today_studies"] = ""
                reply_text(reply_token, KIKUYATU_ITIRAN[2])
            elif "tomorrow_do" not in user_saw[e['source']['userId']]:
                user_saw[e['source']['userId']]["today_studies"] = e['message']['text']
                user_saw[e['source']['userId']]["tomorrow_do"] = ""
                reply_text(reply_token, KIKUYATU_ITIRAN[3])
            elif "quest_for_next" not in user_saw[e['source']['userId']]:
                user_saw[e['source']['userId']]["tomorrow_do"] = e['message']['text']
                user_saw[e['source']['userId']]["quest_for_next"] = ""
                reply_text(reply_token, KIKUYATU_ITIRAN[4])
            else:
                user_saw[e['source']['userId']]["quest_for_next"] = e['message']['text']
                slack_send(user_saw[e['source']['userId']])
                reply_text(reply_token, "投稿しました！お疲れ様でした！")

    return HttpResponse(reply)  # テスト用
