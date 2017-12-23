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


def callback(request):
    reply = ""
    request_json = json.loads(request.body.decode('utf-8'))  # requestの情報をdict形式で取得
    for e in request_json['events']:
        reply_token = e['replyToken']  # 返信先トークンの取得
        message_type = e['message']['type']  # typeの取得

        if message_type == 'text':
            text = e['message']['text']  # 受信メッセージの取得
            reply += reply_text(reply_token, text)  # LINEにセリフを送信する関数
    return HttpResponse(reply)  # テスト用
