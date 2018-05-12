# coding=utf-8
from flask import Blueprint, jsonify, render_template, request

from sdut_spider import SDUT, EduManage
from web_apis.apps.utils import spider_html, schedule_parser

edu_manage_app = Blueprint('edu_manage_app', __name__)


@edu_manage_app.route('/schedule/', methods=['GET', 'POST'])
@edu_manage_app.route('/schedule/<int:cur>/', methods=['GET', 'POST'])
def schedule(cur=None):
    if request.method == 'GET':
        return render_template('query_page.html')
    try:
        user_id = request.form.get('user_id')
        password = request.form.get('password')
        obj = SDUT.get_object(EduManage, user_id, password)
        if not obj:
            return render_template('msg_content.html', message='登录失败，请检查学号与密码')
        data = obj.get_cur_schedule(cur=cur)
        cur = data['cur']
        data['schedule']['data'] = schedule_parser(data['schedule']['data'])
        return render_template('query_html/edu_manage_cur_schedule.html', data=data, cur=cur)
    except Exception:
        return render_template('msg_content.html', message='发生了内部错误，请稍后再试或联系管理员')
