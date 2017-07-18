#Python 1
---
## 中文编码
Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。
解决方法为只要在文件开头加入 

~~~
# -*- coding: UTF-8 -*- 
~~~

或者 

~~~
#coding=utf-8 
~~~

例如代码：

~~~
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
print "你好，世界";
~~~

##行和缩进
&ensp;&ensp;&ensp;&ensp;学习 Python 与其他语言最大的区别就是，Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。python 最具特色的就是用缩进来写模块。

&ensp;&ensp;&ensp;&ensp;缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。如下所示：

~~~
if True:
    print "True"
else:
  print "False"
~~~

##多行语句
&ensp;&ensp;&ensp;&ensp;Python语句中一般以新行作为为语句的结束符。
但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：

~~~
total = item_one + \
        item_two + \
        item_three
~~~

##Python 注释
* python中单行注释采用 # 开头。

~~~
# 这是一个注释
~~~

* python 中多行注释使用三个单引号(''')或三个双引号(""")。

~~~
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""
~~~


