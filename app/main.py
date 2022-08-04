<<<<<<< HEAD
# -*- coding: utf-8 -*-
import json
import random
import os

from flask import Flask, send_file, render_template, jsonify

from app.sys import create_image

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stopwords/<langs>')
def random_stopwords(langs):
    with open(f'stopwords_langs/text/{langs.lower()}.txt', 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
        return random.choice(lines)


@app.route('/stopwords/')
def list_stopwords():
    return render_template('langs.html')


@app.route('/api/stopwords/<langs>', methods=['GET'])
def _json_stopwords(langs):
    with open(f"stopwords_langs/json/{langs.lower()}.json", encoding="utf-8") as f:
        d = json.load(f)
        return jsonify(d)


@app.route('/api/image/<username>/<color>')
def image_created(username, color):
    colors = ['default', 'none', 'none']
    if color in colors:
        create_image(username, color)
        return send_file(f"image/{username}.png", mimetype='image/png')

    else:
        return "Le font n'a pas était trouvé"
=======
# -*- coding: utf-8 -*-
import json
import random
import os

from flask import Flask, send_file, render_template, jsonify

from app.sys import create_image

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stopwords/<langs>')
def random_stopwords(langs):
    with open(f'stopwords_langs/text/{langs.lower()}.txt', 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
        return random.choice(lines)


@app.route('/stopwords/')
def list_stopwords():
    return render_template('langs.html')


@app.route('/api/stopwords/<langs>', methods=['GET'])
def _json_stopwords(langs):
    with open(f"stopwords_langs/json/{langs.lower()}.json", encoding="utf-8") as f:
        d = json.load(f)
        return jsonify(d)


@app.route('/api/image/<username>/<color>')
def image_created(username, color):
    colors = ['default', 'none', 'none']
    if color in colors:
        create_image(username, color)
        return send_file(f"image/{username}.png", mimetype='image/png')

    else:
        return "Le font n'a pas était trouvé"
>>>>>>> 83949628b833b40f402313b309c770639ef05f91
