#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 30/03/2018 2:45 PM
# @Author  : Beer
# @Site    : 
# @File    : Test.py
# @Software: PyCharm
'''
from collections import Counter
class Solution(object):
	def isAnagram(self,s,t):
		"""
		:param s: str
		:param t: str
		:return: bool
		"""
		if len(s) !=len(t):
			return False
		return sorted(s)==sorted(t)
def main(self):
	s="hello world"
	t="worldhello"
	solution = Solution()
	print (solution.isAnagram(s,t))
if __name__=="__main__":
	main()
'''
''' 
#练习输出
name = input()
print("Hello"+name)
'''
'''
#练习list
str="Rorbort"
print(str)
print(str [0:-1])
print(str [0:5:2])
print(str [0:3:2])
'''
'''
#练习list
L=["apple",123,True]
print(L[2])
'''
'''
#练习if循环
breath=input("breath:")
s=int(breath)
if s>2000:
	print("00后")
elif 1900<s<2000:
	print("90后")
elif 1800<s<1900:
	print("80后")
else:
    print("too old")
'''
'''
#练习循环
names=["Tom","Tony","Beer","Sam","Alice"]
for name in names:
	print(name)
'''
'''
#练习range
s=list(range(5))
for n in s:
	print(n)
#错误写法
# for n in list(range(10)):
# 	print (n[1])
'''
'''
#练习dict
d={"Beer":20,"Tom":30,"Alice":40}
# print(d["Beer"])
d["Adam"]=67
d.get("Adam")
d.pop("Beer")
print(d)
'''
'''
#测试自定义函数
def power(x,n):
	#输入类型检查
	if not isinstance(n,(int,float)):
		raise TypeError("bad oprand type")
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s
print(power(5,3))
'''
'''
#函数的参数
#测试默认函数
def add_end(L=[]):
	L.append('end')
	return L
print(add_end([1,2,3]))
print(add_end())
print(add_end())
'''
'''
#定义一个带有可变参数函数
def cacl(*numbers):
	sum=0
	for n in numbers:
		sum=sum+n*n
	return sum
#print(cacl(1,3,4))
#向可变参数函数传入一个可变参数
num=[1,3,4]
print (cacl(*num))
'''
'''
#练习文件输入输出repr
s="Hello,world"
print(s)
print(str(s))
print(repr(s))
x=10*3.25
y=200*200
s1="The value of x is "+repr(x)+",and y is "+repr(y)+"...."
print(s1)
hello="hello world\n"
hellos=repr(hello)
print(hello)
print(hellos)
s2=repr((x,y,('spam','eggs')))
print(s2)
'''
'''
#两种输出格式输出立方和平方
for x in range(1,11):
	print(repr(x).rjust(2),repr(x*x).rjust(3),end='')
	print(repr(x*x*x).rjust(4),)
for x in range(1,11):
	print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))
'''
'''
#测试format

print("we are the {} and {}".format("1","2"))
print('we are the {food} and {advice}'.format(food="sss",advice="bbb"))
table={'Sjoerd': 4127,'Jack': 4098,'Dcab':7678}
for name,phone in table.items():
	print('{0:10} ==> {1:10d}'.format(name,phone))
print('string'.ljust(3)[:1])
'''
'''
#测试操作文件
f=open('/Users/dongwenqi/Desktop/Python/Python','r+')
result=f.read()
result1=f.read(20)
result2=f.readline()
result3=f.readlines()
for line in f:
	line=line.strip()
	print("" % (line))
#print(result)
f.close()
'''
'''
#测试操作文件写入
f=open('/Users/dongwenqi/Desktop/Python/Python','r+')
f.write('\n111111\n')
value=('sdsd',42)
s=str(value)
f.write(s)
for line in f:
	print(line,end='')
print(f.tell())
f.close()
'''
'''
#测试File(文件)方法
f=open('/Users/dongwenqi/Desktop/Python/Python','r+')

print(f.tell())
'''