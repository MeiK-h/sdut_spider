# coding=utf-8
from flask import Blueprint, jsonify, render_template, request

from sdut_spider import SDUT, Logistics
from web_apis.apps.utils import spider_html

logistics_app = Blueprint('logistics_app', __name__)


@logistics_app.route('/energy/', methods=['GET', 'POST'])
def energy():
    if request.method == 'GET':
        return render_template('query_page.html')
    return spider_html(request, Logistics, 'get_energy', 'logistics_energy.html')
