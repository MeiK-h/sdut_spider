# sdut_spider
[SDUT Ehall](http://ehall.sdut.edu.cn/new/ehall.html) Spider


## Warning

The data source of sdut_spider is from various websites within SDUT. If you want to use this project, you must indicate the source of the data in an obvious place.

Data sources and corresponding websites:
- dormitory: [网上服务大厅](http://ehall.sdut.edu.cn/new/ehall.html)
- ecard:     [一卡通自助查询平台](http://211.64.27.136/SelfSearch/Default.aspx)
- ehall:     [网上服务大厅](http://ehall.sdut.edu.cn/new/ehall.html)
- lib:       [山东理工大学图书馆书目检索系统](http://222.206.65.12/reader/redr_info.php)
- logistics: [后勤服务中心](http://hqfw.sdut.edu.cn) (Access exception)
- meol:      [网络教学综合平台](http://211.64.28.63/meol/main.jsp)


## Usage

```python
>>> from sdut_spider import SDUT, Lib
>>> import json
>>> s = SDUT.get_object(Lib, 'user_id', 'password')
>>> print(json.dumps(s.get_borrow_history(), ensure_ascii=False, indent=4))
[
    {
        "barCode": "1767915",
        "title": "悲惨世界",
        "bookUrl": "http://222.206.65.12/opac/item.php?marc_no=0000528614",
        "author": "(法) 维克多·雨果著",
        "borrowDate": "2015-10-18",
        "backDate": "2015-10-29",
        "site": "逸夫馆二层西区"
    },
    {
        "barCode": "208322929",
        "title": "潜水衣与蝴蝶",
        "bookUrl": "http://222.206.65.12/opac/item.php?marc_no=0000142811",
        "author": "(法)让.多米尼克.博比著",
        "borrowDate": "2015-10-18",
        "backDate": "2015-10-29",
        "site": "逸夫馆二层西区"
    },
    {
        "barCode": "2014245",
        "title": "希腊神话传说:权威典藏版",
        "bookUrl": "http://222.206.65.12/opac/item.php?marc_no=0000650141",
        "author": "(德)泼莱勒著",
        "borrowDate": "2015-10-08",
        "backDate": "2015-10-11",
        "site": "逸夫馆二层西区"
    },
    {
        "barCode": "1554967",
        "title": "洛丽塔",
        "bookUrl": "http://222.206.65.12/opac/item.php?marc_no=0000428895",
        "author": "弗拉基米尔·纳博科夫[著]",
        "borrowDate": "2015-09-29",
        "backDate": "2015-10-08",
        "site": "逸夫馆二层西区"
    },
    ......
]
```
