# coding=utf-8
from flask import Blueprint, jsonify, render_template, request

from sdut_spider import SDUT, Dormitory
from web_apis.apps.utils import spider_html

dormitory_app = Blueprint('dormitory_app', __name__)


@dormitory_app.route('/health/', methods=['GET', 'POST'])
def dorm_health():
    if request.method == 'GET':
        return render_template('query_page.html')
    return spider_html(request, Dormitory, 'get_dorm_health', 'dorm_health.html')


@dormitory_app.route('/info/', methods=['GET', 'POST'])
def dorm_info():
    if request.method == 'GET':
        return render_template('query_page.html')
    return spider_html(request, Dormitory, 'get_dorm_info', 'dorm_info.html')
