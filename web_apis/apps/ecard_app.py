# coding=utf-8
import datetime

from flask import Blueprint, jsonify, render_template, request

from sdut_spider import SDUT, Ecard
from web_apis.apps.utils import spider_html

ecard_app = Blueprint('ecard_app', __name__)


@ecard_app.route('/balance/', methods=['GET', 'POST'])
def ecard_balance():
    if request.method == 'GET':
        return render_template('query_page.html')
    return spider_html(request, Ecard, 'get_balance', 'ecard_balance.html')


@ecard_app.route('/consume/', methods=['GET', 'POST'])
def consume_info():
    if request.method == 'GET':
        return render_template('query_page.html')
    return spider_html(request, Ecard, 'get_consume_info', 'ecard_consume.html')


@ecard_app.route('/cust_state_info/', methods=['GET', 'POST'])
@ecard_app.route('/cust_state_info/<int:delta>/', methods=['GET', 'POST'])
def cust_state_info(delta=7):
    if request.method == 'GET':
        return render_template('query_page.html')
    try:
        user_id = request.form.get('user_id')
        password = request.form.get('password')
        obj = SDUT.get_object(Ecard, user_id, password)
        if not obj:
            return render_template('msg_content.html', message='登录失败，请检查学号与密码')
        start = (datetime.date.today() -
                 datetime.timedelta(days=delta)).strftime("%Y%m%d")
        data = obj.get_cust_state_info(start=start)
        return render_template('query_html/cust_state_info.html', data=data, delta=delta)
    except Exception:
        return render_template('msg_content.html', message='发生了内部错误，请稍后再试或联系管理员')
