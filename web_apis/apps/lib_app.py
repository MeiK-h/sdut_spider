# coding=utf-8
from flask import Blueprint, jsonify, render_template, request

from sdut_spider import SDUT, Lib
from web_apis.apps.utils import spider_html

lib_app = Blueprint('lib_app', __name__)


@lib_app.route('/borrow_info/', methods=['GET', 'POST'])
def borrow_info():
    if request.method == 'GET':
        return render_template('query_page.html')
    return spider_html(request, Lib, 'get_borrow_info', 'lib_borrow_info.html')


@lib_app.route('/borrow_history/', methods=['GET', 'POST'])
def borrow_history():
    if request.method == 'GET':
        return render_template('query_page.html')
    return spider_html(request, Lib, 'get_borrow_history', 'lib_borrow_info.html')
