#五、成员资格
#使用in运算符，来判断一值是否在序列中，in运算符是布尔运算符
print("C" in "ChallengerCY" )
print("x" in "ChallengerCY" )
user=["CY","CC","CA"]
#print(input("Enter your user name: ") in user)

#使用in运算符实例
database=[['albert','1234'],['dilbert','4242'],['smith','7524'],['jones','9843']]
#userName=input("User Name: ")
#passWord=input("Pass Word: ")
#if[userName,passWord] in database:
#    print("Pass")


#六、长度(len),最小值(min),最大值(max)
#以上函数除了可以引入序列，还可以直接直接以多个数字(或字符串)直接作为参数
number=[100,200,300]
print(len(number))
print(min(number))
print(max(number))
print(max(2,4,5,6))
print(max("asdcfvbgzA"))

#七 list函数(用于将字符串(所有类型的序列都可以)转换为列表)
print(list("acbsbcsc"))
#通过使用''.join(一个字符组成的列表)转换成字符串
print(''.join(list("acbsbcsc")))

#八、列表的基本操作
#1、改变列表:元素赋值(通过索引赋值，不能为不存在的索引位赋值，可以给None赋值)
x=[1,1,1]
x[1]=2
print(x)
#2、删除元素 使用del(彻底删除,列表的长度也会改变)，del可用的范围比较广
name=["ccc","aaa","bbb"]
del name[2]
print(name)