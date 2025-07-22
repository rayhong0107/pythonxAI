#比較運算子

print(1==2)
print(1!=2)
print(1>=2)
print(1<=2)
print(1>2)
print(1<2)

print(not True)
print(not False)

print(False and False)
print(False and True)
print(True and True)
print(True and True)#ture

print(False or False)
print(False or True)
print(True or False)
print(True and True)#ture

#練習:密碼驗證
password =input("請輸入密碼:")
if password=="1234":
    print("歡迎Ray")
elif password==5678:
    print("歡迎mike")
else:
    print("密碼錯誤")

year=(int(input("請輸入年分:")))
if year % 4== 0 and year %100!=0 or year %400==0:
    print("是閏年")
else:
    print("不是閏年")   