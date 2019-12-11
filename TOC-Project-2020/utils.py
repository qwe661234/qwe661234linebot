import os
import requests

from linebot import LineBotApi, WebhookParser
from linebot.models import *
# from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, 
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

def send_btn_message(reply_token, txt1, txt2, txt3):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='吃吃',
            text='choose',
            thumbnail_image_url='https://raw.githubusercontent.com/qwe661234/qwe661234linebot/master/TOC-Project-2020/img/cxtg.png',
            actions=[
                MessageTemplateAction(
                    label=txt1,
                    text=txt1
                ),
                MessageTemplateAction(
                    label=txt2,
                    text=txt2                                                                                                                                                                                                                                
                ),
                MessageTemplateAction(
                    label=txt3,
                    text=txt3
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_carousel_message(reply_token, txt1, txt2):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text="Carousel template",
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://raw.githubusercontent.com/qwe661234/qwe661234linebot/master/TOC-Project-2020/img/sfg%E5%90%8D.png',
                title="在" + txt1 + "吃吃",
                text='選個',
                actions=[
                    MessageTemplateAction(
                        label='PTT美食',
                        text= txt1 + "批踢踢美食"
                    ),
                    MessageTemplateAction(
                        label='別的地方好了',
                        text='別的地方好了'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://raw.githubusercontent.com/qwe661234/qwe661234linebot/master/TOC-Project-2020/img/sfg%E5%90%8D.png',
                title="在" + txt2 + "吃吃",
                text='選個',
                actions=[
                    MessageTemplateAction(
                        label='PTT美食',
                        text= txt2 + "批踢踢美食"
                    ),
                    MessageTemplateAction(
                        label='別的地方好了',
                        text='別的地方好了'
                    )
                ]
            )
        ]
    )
    )
    line_bot_api.reply_message(reply_token, message)   

    return "OK"

def crawl(page, arg):
    txt = ""
    url = "https://www.ptt.cc/bbs/Food/index.html"
    for i in range(page, page+5):
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        sel = soup.select("div.title a")
        u = soup.select("div.btn-group.btn-group-paging a")
        url = "https://www.ptt.cc"+ u[1]["href"]   
        for s in sel:
            if s.text.find(arg) >= 0:
                title = s.text
                link = "https://www.ptt.cc" + s["href"]
                txt += '{}\n{}\n'.format(title, link)
        
    return txt


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
