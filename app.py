# -*- coding: utf-8 -*-
import json
import random
import os
from PIL import Image, ImageDraw

from flask import Flask, send_file, render_template, jsonify


PEOPLE_FOLDER = os.path.join('static', 'people_photo')
app = Flask(__name__, template_folder='template')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


def create_image(username, font):
    img = Image.new('RGB', (100, 30), color=(73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((10, 10), username, fill=(255, 255, 0))

    img.convert('RGB').save('pil_text.png')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stopwords/<langs>')
def random_stopwords(langs):
    with open(f'stopwords_langs\\text\\{langs}.txt', 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
        return random.choice(lines)


@app.route('/stopwords/')
def list_stopwords():
    return render_template('langs.html')


@app.route('/api/stopwords/<langs>', methods=['GET'])
def _json_stopwords(langs):
    with open(f"stopwords_langs/json/{langs}.json", encoding="utf-8") as f:
        d = json.load(f)
        return jsonify(d)

@app.route('/api/image/<username>/<font>')
def image_created(username, font):
    fonts = ['default', 'none', 'none']
    if font in fonts:
        create_image(username, font)
        return send_file(f"pil_text.png", mimetype='image/png')

    else:
        return "Le font n'a pas était trouvé"

if __name__ == '__main__':
    app.run()
