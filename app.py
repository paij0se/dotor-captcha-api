import glob
from captcha.image import ImageCaptcha
from flask import Flask
from flask import request
from flask import send_file
from time import sleep
import os

app = Flask(__name__)


@app.route('/')
def image():
    # if key doesn't exist, returns None
    ip = request.args.get('ip')
    word = request.args.get('word')
    # http://127.0.0.1:81/?ip=a&word=monda
    sleep(0.5)
    image = ImageCaptcha(width=280, height=90)
    image.write(word, f'{ip}.png')
    print(ip, word)
    return send_file(f'{ip}.png', mimetype='image/png')


removing_files = glob.glob('./*.png')
for i in removing_files:
    os.remove(i)

app.run(host='0.0.0.0', port=81)
