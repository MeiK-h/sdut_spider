# sdut_spider
[SDUT Ehall](http://ehall.sdut.edu.cn/new/ehall.html) Spider


## Usage

```python
>>> from sdut_spider import Ehall, Lib
>>> ehall = Ehall()
>>> ehall.login('username', 'password')
True
>>> lib = Lib(ehall)
>>> lib.logined
True
>>> lib.get_borrow_info()
[]
```
