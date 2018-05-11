# coding=utf-8
from flask import render_template

from web_apis import create_app

app = create_app()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
