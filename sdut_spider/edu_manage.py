# coding=utf-8
import json

from bs4 import BeautifulSoup
from requests import session
from requests.utils import cookiejar_from_dict, dict_from_cookiejar

from .ehall import Ehall


class EduManage(object):
    def __init__(self, ehall):
        if not isinstance(ehall, Ehall) or not ehall.logined:
            print("ehall 必须为已经登录的 Ehall 实例")
            return
        cookies = ehall.cookies
        self.ehall = ehall
        self.session = session()
        self.session.cookies = cookiejar_from_dict(json.loads(cookies))
        self.login()

    def login(self):
        """ 教务管理系统 """
        rst = self.session.get('http://210.44.191.125/jwglxt/jziotlogin')
        if rst.url.startswith('http://210.44.191.125/jwglxt/xtgl/index_initMenu.html'):
            return True
        return False

    @property
    def logined(self):
        """ 检查登录状态 """
        rst = self.session.get(
            'http://210.44.191.125/jwglxt/xtgl/index_initMenu.html')
        if rst.url == 'http://210.44.191.125/jwglxt/xtgl/index_initMenu.html':
            return True
        return False

    def get_schedule(self, year=-1, semester=-1, parse=True):
        """ 获得个人课表 """
        # 若不填写年份与学期，则按照默认的查询（最近要上的课表）
        url = 'http://210.44.191.125/jwglxt/xkcx/xkmdcx_cxXkmdcxIndex.html?doType=query'
        data = {
            'queryModel.showCount': '100',  # 要是有哪位同学一个学期的课程超过一百门...那就节哀吧
            'queryModel.currentPage': '1',
            'time': '0',
        }
        if year == -1:
            return None
        data['xnm'] = str(year)
        if semester == -1:
            return None
        if semester == 1:
            data['xqm'] = '3'
        elif semester == 2:
            data['xqm'] = '12'
        else:
            return None

        rst = self.session.post(url, data=data)
        rjson = json.loads(rst.text)
        if not rjson['items']:
            return None
        if parse:  # 若指定信息 parse，则解析数据
            rdata_list = []
            for i in rjson['items']:
                d = {
                    'year': i.get('xnmc', ''),
                    'semester': i.get('xqmc', ''),
                    'course_code': i.get('kch_id', ''),
                    'course_name': i.get('kcmc', ''),
                    'score': i.get('xf', ''),
                    'state': i.get('kkztmc', ''),
                    'class_time': i.get('sksj', ''),
                    'class_location': i.get('jxdd', ''),
                    'course_category': i.get('kclbmc', ''),
                    'course_nature': i.get('kcxzmc', ''),
                    'course_type': i.get('kklxmc', ''),
                    'class': i.get('jxbmc', ''),
                }
                if i.get('jsxx'):  # parse 任课教师
                    _tmp = i.get('jsxx').split('/')
                    if len(_tmp) == 3:
                        _bh, _xm, _zc = _tmp
                    else:
                        _bh, _xm = _tmp
                        _zc = 'None'
                    d['teacher'] = {
                        'id': _bh,
                        'name': _xm,
                        'title': _zc
                    }
                if i.get('sksj', ''):  # parse 上课时间地点
                    _sj = i.get('sksj', '').split(';')
                    _dd = i.get('jxdd', '').split(';')
                    cnt = len(_sj)
                    _sjdd = []
                    for i in range(cnt):
                        _sj_s = _sj[i].split('{')
                        _sjdd.append({
                            'time': _sj_s[0],
                            'location': _dd[i],
                            'week': _sj_s[1][:-1]
                        })
                    d['time_location'] = _sjdd
                rdata_list.append(d)
            rdata = {
                'data': rdata_list,
                'name': rjson['items'][0].get('xm'),
                'sex': rjson['items'][0].get('xbmc'),
                'stuid': rjson['items'][0].get('xh_id'),
                'grade': rjson['items'][0].get('njdm_id'),
                'major': rjson['items'][0].get('zymc'),
                'class': rjson['items'][0].get('bjmc')
            }
            return rdata
        else:  # 否则以原始形式返回
            return rjson
