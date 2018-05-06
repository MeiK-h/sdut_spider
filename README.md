# sdut_spider
[SDUT Ehall](http://ehall.sdut.edu.cn/new/ehall.html) Spider


## Usage

```python
>>> from sdut_spider import Ehall, Lib, Dormitory, Logistics
>>> ehall = Ehall()
>>> ehall.login('username', 'password')
True
>>> lib = Lib(ehall)
>>> lib.logined
True
>>> lib.get_borrow_info()
[]
>>> dormitory = Dormitory(ehall)
>>> dormitory.logined
True
>>> dormitory.get_dorm_health()
[...]
>>> logistics = Logistics(ehall)
>>> logistics.get_energy()
{'room': '01#233', 'date': '2000-00-00 00:00:00', 'energy': '233', 'lower': '233', 'upper': '233', 'status': '正常用电'}
>>> meol = Meol(ehall)
>>> meol.get_reminder()
{'notice': [{'url': 'http://211.64.28.63/meol/../../lesson/enter_course.jsp?lid=13747&t=info', 'title': '编译原理(A)'}], 'work': [{'url': 'http://211.64.28.63/meol/../../lesson/enter_course.jsp?lid=17318&t=hw', 'title': '统一建模语言UML(A)'}, {'url': 'http://211.64.28.63/meol/../../lesson/enter_course.jsp?lid=28774&t=hw', 'title': 'Java Web程序设计(A)'}]}
```
