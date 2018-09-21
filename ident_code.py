#!/usr/bin/python env
# coding:utf-8
import random
#四位数随机验证码 A-Z 65-90 a-z 97-122 0-9
def ident_code(num=4):
    res = ""
    for i in range(num):
        num1 = str(random.randint(0,9))
        a = chr(random.randint(65,90))
        b = chr(random.randint(97,122))
        res += random.choice([num1,a,b])
    return  res
print(ident_code())
