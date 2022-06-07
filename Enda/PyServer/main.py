from flask import Flask, render_template
from threading import Thread

app = Flask('')


@app.route('/')
def home():
    return render_template('index.html')


def run():
    app.run(host="0.0.0.0")


def keep_alive():
    server = Thread(target=run)
    server.start()


keep_alive()
