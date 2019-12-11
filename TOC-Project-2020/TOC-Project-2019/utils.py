import requests
from bs4 import BeautifulSoup

GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAIGxJRriXUBAHQfMGPC3b4iwJNZBSKR7GM0DY1MqSrHAhzZBZCT1ABRUshJr5ZAjLJPJMED5prDQG7ZCmDKXzZCOgZAzJjCxyIM6JjOaBtDPOvXZBC4HC1dWcRZBzZBN471J3Ga4OyAIZCOzksFRlNMh2LeQDWDYnz3CglnZAxXxRu8kQZDZD"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_btn_message(id, text, btn):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
      "recipient": {"id": id},
      "message":{
        "attachment":{
        "type":"template",
        "payload":{
          "template_type":"button",
          "text":text,
          "buttons":btn
        }
      }
    }
  }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

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
