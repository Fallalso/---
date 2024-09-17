#判断输入类型
#如果10进制
#如果二进制
variable = input('二进制转十进制输入2\n十进制转二进制输入10\n:')
if variable==2:
    ten1 = input('输入待转换数字:')
    ten = int(ten1,2)
    print(ten)
else:
    two1 = input('输入待转换数字:')
    two = bin(int(two1,10))[2:]
    print(two)
