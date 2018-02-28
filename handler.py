import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "./vendored"))

import requests

TOKEN = os.environ['TELEGRAM_TOKEN']
BASE_URL = "https://api.telegram.org/bot{}".format(TOKEN)


def hello(event, context):
    try:
        data = json.loads(event["body"])
        mensaje = str(data["message"]["text"])
        chat_id = data["message"]["chat"]["id"]
        primer_nombre = data["message"]["chat"]["first_name"]

        respuesta = "Please /start, {}".format(first_name)

        data = {"text": respuesta.encode("utf8"), "chat_id": chat_id}
        url = BASE_URL + "/sendMessage"
        requests.post(url, data)

    except Exception as e:
        print(e)

    return {"statusCode": 200}
