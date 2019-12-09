import os
import requests
from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
from bs4 import BeautifulSoup

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_image_message(reply_token, url):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, ImageSendMessage(original_content_url=url, preview_image_url=url))

    return "OK"

def send_btn_message(reply_token, txt):
    line_bot_api = LineBotApi(channel_access_token)
    message = {
        "type": "template",
        "altText": "在不支援顯示樣板的地方顯示的文字",
        "template": {
            "type": "buttons",
            "text": "eat",
            "actions": [
            {
                "type": "message",
                "label": "eat",
                "text": "eee"
            }
            ]
        }
    }
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def crawl(arg):
    txt = ""
    if arg == "台北":
        keyword = "台北"
    elif arg == "高雄":
        keyword = "高雄"
    url = "https://www.ptt.cc/bbs/Food/index.html"
    for i in range(10):
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        sel = soup.select("div.title a")
        u = soup.select("div.btn-group.btn-group-paging a")
        url = "https://www.ptt.cc"+ u[1]["href"]   
        for s in sel:
            if s.text.find(keyword) >= 0:
                title = s.text
                link = "https://www.ptt.cc" + s["href"]
                txt += '{}\n{}\n'.format(title, link)
        
    return txt

a = crawl("台北")
print(a)

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
