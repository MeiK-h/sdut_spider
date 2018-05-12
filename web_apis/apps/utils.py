# coding=utf-8
import operator
from flask import render_template

from sdut_spider import SDUT


def spider_html(request, clas, func, temp):
    try:
        user_id = request.form.get('user_id')
        password = request.form.get('password')
        obj = SDUT.get_object(clas, user_id, password)
        if not obj:
            return render_template('msg_content.html', message='登录失败，可能是学号与密码错误，也有可能是对应的网站出问题了')
        data = getattr(obj, func)()
        return render_template('query_html/' + temp, data=data)
    except Exception:
        return render_template('msg_content.html', message='发生了内部错误，请稍后再试或联系管理员')


def schedule_parser(schedule):
    week_list = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    rdata = []
    # 拆分所有课时
    for i in schedule:
        for j in i['time_location']:
            k = i.copy()
            k['time_location'] = j
            rdata.append(k)
    rdata = sorted(rdata, key=lambda x: (week_list.index(
        x['time_location']['time'][:3]), find_first_number(x['time_location']['time'])))
    return rdata


def find_first_number(s):
    s = s.split('-')[0]
    return int(s[4:])
