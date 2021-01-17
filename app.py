import os
from flask import Flask
from TwitterCoronaApp import views

app = Flask(__name__)


@app.route("/")
def hello(request):
    return views.home(request)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
