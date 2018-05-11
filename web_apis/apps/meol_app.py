# coding=utf-8
from flask import Blueprint, jsonify, render_template, request

from sdut_spider import SDUT, Meol
from web_apis.apps.utils import spider_html

meol_app = Blueprint('meol_app', __name__)


@meol_app.route('/reminder/', methods=['GET', 'POST'])
def reminder():
    if request.method == 'GET':
        return render_template('query_page.html')
    return spider_html(request, Meol, 'get_reminder', 'meol_reminder.html')
