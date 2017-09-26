# -*- coding: utf-8 -*-

list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ,6,5,5];

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])


# 删除 元素

# del list[2]

'''
序号	函数
1	len(list)
列表元素个数
2	max(list)
返回列表元素最大值
3	min(list)
返回列表元素最小值
4	list(seq)
将元组转换为列表
'''
#在列表末尾添加新的对象
list1.append("hahah")
print(list1)

#统计某个元素在列表中出现的次数
print(list2.count(5))

# 从列表中找出某个值第一个匹配项的索引位置
print(list1.index("hahah"))

# 将对象插入列表
list1.insert(2,"lalal")
print(list1)

# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

print(list1.pop())





















