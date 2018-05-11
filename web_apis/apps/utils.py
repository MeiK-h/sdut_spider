# coding=utf-8
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
