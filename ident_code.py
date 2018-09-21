#!/usr/bin/python env
# coding:utf-8
def ident_code(num=4):
    res = ""
    for i in range(num):
        num1 = str(random.randint(0,9))
        a = chr(random.randint(65,90))
        b = chr(random.randint(97,122))
        res += random.choice([num1,a,b])
    return  res
print(ident_code())
