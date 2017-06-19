#6、pop方法会移除列表中的一个元素(默认是最后一个)，并且返回该元素值,使用pop方法可以栈，栈是常见的数据结构(先进后出)
number=[1,2,3,4,5,6]
print(number.pop())
print(number)
#Python中没有push()入栈的方法，可以使用append方法代替
number.append(number.pop())
print(number)
#简单的队列(queue)(先进先出)实现
number.insert(0,number.pop(0))
print(number)

#7、remove方法，用于移除列表中某个值的第一个匹配项
number2=[1,2,3,4,5,6,2]
number2.remove(2)
print(number2)

#8、reverse方法将列表中的元素反向存放
number3=[1,2,3,4,5,6]
number3.reverse()
print(number3)
#需要对一个数序列进行反向迭代，可以使用reversed函数，该函数返回一个迭代器，可以用list进行转换
print(list(reversed(number3)))

#9、sort方法用于列表的排序(sort方法直接修改原序列，而不会简单的返回一个已经排序的列表副本)
number4=[1,4,5,7,8,2,3,6]
number4.sort()
print(number4)
#如果需要保存原序列，还需要一个排好序的副本,参考以下方法（y=x[:]是一种很有效率的复制整个列表的方法，简单的=赋值没有用，会指向同一个列表）:
number5=[1,4,5,7,8,2,3,6]
y=number5[:]
y.sort()
print(number5)
print(y)
#还有一种方法，使用sorted函数(这个函数可以用于任何序列，并且返回一个列表)
number6=[1,2,3,5,6,9,8,7]
y=sorted(number6)
print(number6)
print(y)
print(sorted("python"))