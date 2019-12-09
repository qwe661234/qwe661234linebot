from transitions.extensions import GraphMachine
from utils import send_text_message, send_image_message, send_btn_message, crawl

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    
    def is_going_to_eat(self, event):
        text = event.message.text
        return text.lower() == "吃吃"

    def on_enter_eat(self, event):
        print("I'm entering eat")
        reply_token = event.reply_token
        send_btn_message(reply_token, "高雄 or 台北")
        self.go_back()
    
    def on_exit_eat(self):
        print("Leaving eat")
    
    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "高雄"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "台北"

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "image"

    def on_enter_state1(self, event):
        print("I'm entering state1")
        txt = crawl("高雄")
        reply_token = event.reply_token
        send_text_message(reply_token, txt)
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")
        txt = crawl("台北")
        reply_token = event.reply_token
        send_text_message(reply_token, txt)
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_image_message(reply_token, 'https://qwe661234linebot.herokuapp.com/show-fsm')
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")
