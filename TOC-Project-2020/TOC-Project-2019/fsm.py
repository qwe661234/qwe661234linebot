from transitions.extensions import GraphMachine

from utils import send_text_message, send_btn_message, crawl


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'go to state1'
        return False

    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering state1")
        self.go_back()

    def on_exit_state1(self):
        print('Leaving state1')

    def is_going_to_state2(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == '吃吃'
        return False
    
    def on_enter_state2(self, event):
        print("I'm entering state2")
        sender_id = event['sender']['id']
        btn = [
            {
              "type": "postback",
              "title": "北部",
              "payload": "北部"
            },
            {
              "type": "postback",
              "title": "南部",
              "payload": "南部"
            }
        ]
        send_btn_message(sender_id, "選個", btn)
    
    def is_going_to_north(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text == '北部'
        return False

    def on_enter_north(self, event):
        sender_id = event['sender']['id']
        btn = [
            {
                "type": "postback",
                "title": "台北",
                "payload": "台北"
            },
            {
                "type": "postback",
                "title": "桃園",
                "payload": "桃園"
            },
        ]
        send_btn_message(sender_id, "選個", btn)

    def is_going_to_south(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text == '南部'
        return False

    def on_enter_south(self, event):
        sender_id = event['sender']['id']
        btn = [
            {
                "type": "postback",
                "title": "台南",
                "payload": "台南"
            },
            {
                "type": "postback",
                "title": "高雄",
                "payload": "高雄"
            },
        ]
        send_btn_message(sender_id, "選個", btn)

    def is_going_to_tainan(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text == '台南'
        return False
    
    def on_enter_tainan(self, event):
        print("I'm entering state1")
        msg = crawl(1, "台南")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, msg)
        self.go_back()

    def on_exit_tainan(self):
            print('Leaving tainan')
    
    def is_going_to_kaohsiung(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text == '高雄'
        return False
    
    def on_enter_kaohsiung(self, event):
        print("I'm entering kaohsiung")
        msg = crawl(1, "高雄")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, msg)
        self.go_back()

    def on_exit_kaohsiung(self):
            print('Leaving kaohsiung')
    
    def is_going_to_taipei(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text == '台北'
        return False
    
    def on_enter_taipei(self, event):
        print("I'm entering state1")
        msg = crawl(1, "台北")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, msg)
        self.go_back()

    def on_exit_taipei(self):
            print('Leaving taipei')
    def is_going_to_taoyuan(self, event):
        if event.get("postback"):
            if event['postback'].get('payload'):
                text = event['postback']['payload']
                return text == '桃園'
        return False
    
    def on_enter_taoyuan(self, event):
        print("I'm entering state1")
        msg = crawl(1, "桃園")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, msg)
        self.go_back()

    def on_exit_taoyuan(self):
            print('Leaving taoyuan')