#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Python 练习栗子
'''

# 打印随机数
import random

print random.random() # 输出0-1之间的随机数
print random.uniform(10,50) 
print random.randint(1,100) #随机整数


# 位运算
# if __name__ == '__main__':
#     a = 077
#     b = a & 3
#     print 'a & b = %d' % b
#     b &= 7
#     print 'a & b = %d' % b


if __name__ == '__main__':
    a = int(raw_input('input a number:\n'))
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    print '%o\t%o' %(a,d)