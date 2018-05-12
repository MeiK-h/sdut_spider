# coding=utf-8
from flask import Flask


def create_app():
    app = Flask(__name__)

    from web_apis.apps import dormitory_app
    app.register_blueprint(dormitory_app, url_prefix='/dormitory')

    from web_apis.apps import ecard_app
    app.register_blueprint(ecard_app, url_prefix='/ecard')

    from web_apis.apps import lib_app
    app.register_blueprint(lib_app, url_prefix='/lib')

    from web_apis.apps import logistics_app
    app.register_blueprint(logistics_app, url_prefix='/logistics')

    from web_apis.apps import meol_app
    app.register_blueprint(meol_app, url_prefix='/meol')

    from web_apis.apps import edu_manage_app
    app.register_blueprint(edu_manage_app, url_prefix='/edu_manage')

    return app
