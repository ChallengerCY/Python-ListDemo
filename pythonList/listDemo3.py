#通用序列操作

#二、分片
#分片用于索引一定范围内的元素使用方法是[a:b],以a开始索引，以b-1结束
message1="abcdefghijklmn"
print(message1[1:9])
#同样可以使用负数，代表反向索引
print(message1[1:-6])
#获取末尾的元素
print(message1[-1:])
#获取第一个元素
print(message1[:1])
#获取整个序列
print(message1[:])
#更大的步长[::X]x代表跳跃的个数，可以是负数
print(message1[1:9:2])
print(message1[9:1:-2])

#三、序列的相加(只支持同类型序列直接相加)
print([1,2,3]+[4,5,6])
print("hello "+"world")

#四、序列的乘法
#使用一个序列乘以一个整数会得到相应数量的序列
print(message1*2)
print([7]*10)
#使用None来初始化一个长度为10的列表，None是Python的一个内键值，确切的含义是这里面没有东西
sequence=[None]*10
print(sequence)