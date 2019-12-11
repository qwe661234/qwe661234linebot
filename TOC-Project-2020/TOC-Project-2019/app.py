from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = "123"
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'north',
        'south',
        'tainan',
        'kaohsiung',
        'taipei',
        'taoyuan'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'north',
            'conditions': 'is_going_to_north'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'south',
            'conditions': 'is_going_to_south'
        },
        {
            'trigger': 'advance',
            'source': 'south',
            'dest': 'kaohsiung',
            'conditions': 'is_going_to_kaohsiung'
        },
        {
            'trigger': 'advance',
            'source': 'south',
            'dest': 'tainan',
            'conditions': 'is_going_to_tainan'
        },
        {
            'trigger': 'advance',
            'source': 'north',
            'dest': 'taipei',
            'conditions': 'is_going_to_taipei'
        },
        {
            'trigger': 'advance',
            'source': 'north',
            'dest': 'taoyuan',
            'conditions': 'is_going_to_taoyuan'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'kaohsiung',
                'tainan',
                'taipei',
                'taoyuan'
            ],
            'dest': 'user'
        },
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="0.0.0.0", port=5000, debug=True)
