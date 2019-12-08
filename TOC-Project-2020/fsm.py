from transitions.extensions import GraphMachine
from utils import send_text_message, send_image_message

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "test"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "news"

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "image"

    def on_enter_state1(self, event):
        print("I'm entering state1")
        txt="TTT"
        reply_token = event.reply_token
        send_text_message(reply_token, txt)
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "news")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_image_message(reply_token, 'https://mmbiz.qpic.cn/mmbiz_jpg/odMCwmIOg7E1yP6PctYTewHuUxSFWHIyibkIKnEYJ5jjX727GtI9WBibBz8ib6KT8G99B4wyJrZ9PPIByk3d37icIQ/640?wx_fmt=jpeg')
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")
