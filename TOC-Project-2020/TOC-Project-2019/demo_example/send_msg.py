import os
import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = os.environ.get("EAAv4MBh4nD8BACIiDI7NmW3IjHNtZCcXTAMGEJFHaBS1DLpOkeIRNGVwSup08fyr2WjBak6Y8ZC2FlqCeTe3UG0N43IFtnmjNK0rIVfQxN4BigTKSr8NKNLiWabdstUI3CpYPR4etSnTAw85CyygxHZB8oZB5mFDWnnjVyC1CwZDZD")


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response.text
