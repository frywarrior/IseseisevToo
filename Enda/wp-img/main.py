from flask import Flask, render_template
from threading import Thread
from GetImg import getimg
import time

app = Flask('')


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


def run():
    app.run(host="0.0.0.0")



def keep_alive():
    server = Thread(target=run)
    server.start()


keep_alive()

while True:
    getimg()
    time.sleep(300)