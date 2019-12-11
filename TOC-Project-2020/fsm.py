from transitions.extensions import GraphMachine
from utils import send_text_message, send_image_message, send_btn_message, send_carousel_message, crawl

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    
    def is_going_to_eat(self, event):
        text = event.message.text
        if text.lower() == "吃吃" or text.lower() == "別的地方好了":
            return 1
        else:
            return 0

    def is_going_to_north(self, event):
        text = event.message.text
        return text.lower() == "北部"
    
    def is_going_to_middle(self, event):
        text = event.message.text
        return text.lower() == "中部"
 
    def is_going_to_south(self, event):
        text = event.message.text
        return text.lower() == "南部"

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "image"
    
    def is_going_to_taipei(self, event):
        text = event.message.text
        return text.lower() == "台北批踢踢美食"
    
    def is_going_to_taoyuan(self, event):
        text = event.message.text
        return text.lower() == "桃園批踢踢美食"

    def is_going_to_taichung(self, event):
        text = event.message.text
        return text.lower() == "台中批踢踢美食"
    
    def is_going_to_changhua(self, event):
        text = event.message.text
        return text.lower() == "彰化批踢踢美食"
    
    def is_going_to_tainan(self, event):
        text = event.message.text
        return text.lower() == "台南批踢踢美食"
           
    def is_going_to_kaohsiung(self, event):
        text = event.message.text
        return text.lower() == "高雄批踢踢美食"

    def on_enter_eat(self, event):
        print("I'm entering eat")
        reply_token = event.reply_token
        send_btn_message(reply_token, "北部", "中部", "南部")

    def on_enter_north(self, event):
        print("I'm entering north")
        reply_token = event.reply_token
        send_carousel_message(reply_token, "台北", "桃園")
    
    def on_enter_middle(self, event):
        print("I'm entering middle")
        reply_token = event.reply_token
        send_carousel_message(reply_token, "台中", "彰化")

    def on_enter_south(self, event):
        print("I'm entering south")
        reply_token = event.reply_token
        send_carousel_message(reply_token, "台南", "高雄")

    def on_enter_tainan(self, event):
        print("I'm entering tainan")
        msg = crawl(1, "台南")
        reply_token = event.reply_token
        send_text_message(reply_token, msg)
        self.go_back()
        
    def on_exit_tainan(self):
        print("Leaving tainan")
    
    def on_enter_kaohsiung(self, event):
        print("I'm entering kaohsiung")
        msg = crawl(1, "高雄")
        reply_token = event.reply_token
        send_text_message(reply_token, msg)
        self.go_back()

    def on_exit_kaohsiung(self):
        print("Leaving kaohsiung")
    
    def on_enter_taichung(self, event):
        print("I'm entering taichung")
        msg = crawl(1, "台中")
        reply_token = event.reply_token
        send_text_message(reply_token, msg)
        self.go_back()

    def on_exit_taichung(self):
        print("Leaving taichung")
    
    def on_enter_changhua(self, event):
        print("I'm entering changhua")
        msg = crawl(1, "彰化")
        reply_token = event.reply_token
        send_text_message(reply_token, msg)
        self.go_back()

    def on_exit_changhua(self):
        print("Leaving changhua")
    
    def on_enter_taipei(self, event):
        print("I'm entering taipei")
        msg = crawl(1, "台北")
        reply_token = event.reply_token
        send_text_message(reply_token, msg)
        self.go_back()

    def on_exit_taipei(self):
        print("Leaving taipei")
    
    def on_enter_taoyuan(self, event):
        print("I'm entering taoyuan")
        msg = crawl(1, "桃園")
        reply_token = event.reply_token
        send_text_message(reply_token, msg)
        self.go_back()

    def on_exit_taoyuan(self):
        print("Leaving taoyuan")

    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_image_message(reply_token, 'https://qwe661234linebot.herokuapp.com/show-fsm')
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")

