# -*- coding: utf-8 -*-


var_1 = "Hellow world"
var_2 = "Python"

print("---: ",var_1[1:5])
print("",var_2[0])

print ("已更新字符串 : ", var_1[:6] + var_2)

a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if ("H" in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if ("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print(r'\n')
print(R'\n')

# 字符串格式化

print("我叫 %s ,几年 %d 岁" % ("hahh",23))


num=18.7254
print("the price  is  %.2f" %num)    #the price  is  18.73

#------------------------------------------------------------------------------------------------------------------
print("--------------------------------------------------------------------------------------------------------------")


str = "hello world"

#将字符串的第一个字符转换为大写
print(str.capitalize())

#返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
print(str.center(20, "*"))  #****hello world*****

#返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数#
print(str.count("l",0,10))

'''
#decode() 方法以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。
str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
print(str)
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))
'''


#检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
print(str.endswith("o",0,len(str)))
print(str.endswith("d",0,len(str)))



#把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。

string = "hha   哈哈      hha"
print(string.expandtabs(0))


#检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
print(str.find("l",1))

#跟find()方法一样，只不过如果str不在字符串中会报一个异常

print(str.index("l"))

str = "aaakll"
#如果字符串 至少有一个字符 并且 所有字符 都是字母或数字则返 回 True,否则返回 False
print(str.isalnum())
#如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
print(str.isalpha())

str = "sjk123"
#如果字符串只包含数字则返回 True 否则返回 False..
print(str.isdigit())