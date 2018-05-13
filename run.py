# coding=utf-8
from flask import render_template, request

from web_apis import create_app
from sdut_spider import get_user_list

app = create_app()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/analytics/', methods=['GET', 'POST'])
def analytics():
    if request.method == 'GET':
        return render_template('query_page.html')
    data = get_user_list()
    return render_template('analytics.html', data=data, cnt=len(data))


if __name__ == '__main__':
    app.run(debug=True)
