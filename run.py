# coding=utf-8
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

from sdut_spider import (SDUT, Dormitory, Ecard, EduManage, Ehall, Lib,
                         Logistics, Meol)
from web_apis import create_app

app = create_app()
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
