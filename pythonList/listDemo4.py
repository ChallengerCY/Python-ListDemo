#序列(字符串)乘法示例
#以正确的宽度在居中的盒子内打印一个句子
#//整数除法运算符(//)支持python 2.2以后的版本

message=input("Message: ")
screen_width=80
text_width=len(message)
box_width=text_width+6
left_margin=(screen_width-box_width)//2

print()
print(''*left_margin+'+'+'-'*(box_width-2)+ '+')
print(''*(left_margin+4)+'|'+' '*text_width      +'|')
print(''*(left_margin+4)+'|'+   message      +'|')
print(''*(left_margin+4)+'|'+' '*text_width      +'|')
print(''*left_margin+'+'+'-'*(box_width-2)+ '+')