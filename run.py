# coding=utf-8
from flask import Flask, jsonify, request, render_template

from sdut_spider import (SDUT, Dormitory, Ecard, EduManage, Ehall, Lib,
                         Logistics, Meol)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


class_dict = {
    'Dormitory': Dormitory,
    'Ecard': Ecard,
    'EduManage': EduManage,
    'Ehall': Ehall,
    'Lib': Lib,
    'Logistics': Logistics,
    'Meol': Meol
}


@app.route('/', methods=['POST'])
def api():
    user_id = request.form.get('user_id')
    password = request.form.get('password')
    clas = request.form.get('class')
    func = request.form.get('func')
    if user_id and password and clas and func:
        obj = SDUT.get_object(class_dict[clas], user_id, password)
        if not obj:
            return jsonify({'state': 'error', 'msg': 'login failure'})
        data = getattr(obj, func)()
        return jsonify({'state': 'success', 'data': data})
    return jsonify({
        'data': {
            'user_id': user_id,
            'password': password,
            'class': clas,
            'func': func
        },
        'state': 'error'
    })


@app.route('/<clas>/')
def get_class_func(clas):
    l = dir(class_dict[clas])
    func = []
    for i in l:
        if i.startswith('get_'):
            func.append(i)
    return jsonify({
        'state': 'success',
        'data': func
    })


if __name__ == '__main__':
    app.run(debug=True)
