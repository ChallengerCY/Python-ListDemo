#序列的概述
#列表中的各个元素通过逗号分隔，写在[]中

#一、普通的列表
list1=['age',2]
print (list1)

#二、包含其他列表的列表
list2=['age',2]
list3=['name','CY']
database=[list2,list3]
list4=database[1]
print(database)
print(list4)

#说明序列(列表和元组)中每个元素都有自己的编号,映射(字典)每个元素都有自己的名字(也称为键)，集合(set)既不是序列也不是映射

#通用序列操作

#一、索引
#索引[0]指向第一个元素，使用负数索引时,Python会从最后一个元素开始计数，最后一个元素的编号是-1
message1='Hello'
print(message1[0])
print(message1[-5])

#字符串字面值(或其他的序列字面量)可直接使用索引，不需要变量的引用
print("ChallengerCY"[7])

#如果函数调用返回一个序列，那么可以对返回结果进行索引操作
message2=input("year:")[3]
print(message2)



