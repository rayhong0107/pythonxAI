import streamlit as st

'''
多
行
注
解
'''
#這是多行註解

print(1234) #輸出整數
print(1.234) #輸出浮點數
print(False) #輸出布林值
print(True) #輸出布林值
print("hello world") #輸出字串
a = 10 #定義變數a
print(a) #輸出變數a
a = 20 #重新定義變數a
print(a) #輸出變數a
a= "apple" 
print(a)
x=4
x=x+5
print(x) 
x=x**4

print(x)
print(x+x+8)#加法
print(x-1)#減法
print(x*2)#乘法
print(x/2)#除法
print(x//20)#整除
print(x%3)#取餘數
print(x**2) #指數運算
v1=.1
v2=.2
print(v1+v2) #浮點數加法

s1="hello"
s2="world"
print(s1 +" " + s2 *3)
name="python"
age=30
new_str=f"我是{name}今年{age}歲"
print(new_str) #格式化字串輸出

print(len(""))
print(len("hello"))

print(type (True))# 布林值類型
print(type (5))# 整數類型
print(type ("hello"))# 字串類型
print(type (.5))# 浮點數類型

print(int(True))
print(int(123))
# print(int("hello")) # 這行會報錯，因為不能將字串轉換為整數

print(float(True))
print(float(123))
# print(float("hello")) # 這行會報錯，因為不能將字串轉換為浮點數

print(bool(0)) #false
print(bool(1)) #true
print(bool("hello")) #true
print(bool(-2)) #true
print(bool("")) # false

print(str(True))
print(str(123))
print(str("hello"))

# c=input()
c=input("請輸入你的名字：")
print("原來是" + c +"啊！")
print(type(c))

d=input("圓的半徑是多少ˇ")
print("圓的面積是"+ str(3.14 * float(d) ** 2))