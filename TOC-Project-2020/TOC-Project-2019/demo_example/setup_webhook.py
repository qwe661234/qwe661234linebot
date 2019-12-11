from bottle import route, run, request


VERIFY_TOKEN = "EAAv4MBh4nD8BACIiDI7NmW3IjHNtZCcXTAMGEJFHaBS1DLpOkeIRNGVwSup08fyr2WjBak6Y8ZC2FlqCeTe3UG0N43IFtnmjNK0rIVfQxN4BigTKSr8NKNLiWabdstUI3CpYPR4etSnTAw85CyygxHZB8oZB5mFDWnnjVyC1CwZDZD"


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

run(host="localhost", port=5000, debug=True)
