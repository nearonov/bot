# from flask import Flask, request
# from flask.views import MethodView
#
#
# app = Flask(__name__)
#
# @app.route('/', methods=["POST", "GET"])
# def index():
#     if request.method == "POST":
#         resp = request.get_json()
#         print(resp)
#         return '<h1>Hi Telegram</h1>'
#     return '<h1>Hi Bot</h1>'
#
#
# class BotAPI(MethodView):
#     def get(self):
#         return '<h1>Hi Bot_Class</h1>'
#
#     def post(self):
#         resp = request.get_json()
#         print(resp)
#         return '<h1>Hi Telegram_Class</h1>'
#
#
# app.add_url_rule('/TOKEN/', view_func=BotAPI.as_view('bot'))
#
# if __name__ == "__main__":
#     app.run()


import requests
import os
from dotenv import load_dotenv
from flask import Flask, request
from flask.views import MethodView

load_dotenv()

app = Flask(__name__)
TOKEN = os.environ.get('TOKEN')
TELEGRAM_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'


def send_message(chat_id, msg):
    session = requests.Session()
    r = session.get(TELEGRAM_URL, params=dict(chat_id=chat_id,
                                              text=msg,
                                              parse_mode='Markdown'))
    return r.json()


def parse_text(text_msg):
    if '/' in text_msg:
        if '/start' in text_msg or '/help' in text_msg:
            message = '''Для того, чтобы узнать, какие города доступны, отправьте в сообщении `/city`.
            Чтобы узнать о доступных специальностях - отправьте `/sp`
            Чтобы сделать запрос на сохраненные вакансии, отправьте в сообщении через пробел - @город @специальность.
            Например так - `@kyiv @python`  '''
            return message
    else:
        return None


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        resp = request.get_json()
        print(resp)
        return '<h1>Hi Telegram</h1>'
    return '<h1>Hi Bot</h1>'


class BotAPI(MethodView):

    def get(self):
        return '<h1>Hi Bot_Class</h1>'

    def post(self):
        resp = request.get_json()
        text_msg = resp['message']['text']
        chat_id = resp['message']['chat']['id']
        tmp = parse_text(text_msg)
        if tmp:
            send_message(chat_id, tmp)
        print(resp)
        return '<h1>Hi Telegram_Class</h1>'




app.add_url_rule('/TOKEN/', view_func=BotAPI.as_view('bot'))

if __name__ == "__main__":
    app.run()



