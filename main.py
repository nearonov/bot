from flask import Flask, request
from flask.views import MethodView

app = Flask(__name__)


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
        print(resp)
        return '<h1>Hi Telegram_Class</h1>'

app.add_url_rule('/TOKEN/',view_func=BotAPI.as_view('bot'))

if __name__ == "__main__":
    app.run()



