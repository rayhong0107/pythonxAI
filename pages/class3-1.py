l=["a", "b", "c"]
for element in l:
    print(element)

print('-'*20)

print(len([]))
print(len(['蘋果']))
print(len(['a','b''c']))
print(len([1,2,3]))

print('-'*20)

for i in range(len(l)):
    print(l[i])

print('-'*20)

a=[1,2,3]
b=a
b[0]=2
print(a)

print('-'*20)

a=[1,2,3]
b=a[:]
b[0]=2
print(a)

print('-'*20)

l[0]="A"
l[1]="D"
print(l)

print('-'*20)

r=[22,1,3,4,1,2,]
r.append(5)#新增在最後一項
print(r)

print('-'*20)

r.pop()#移除最後一項
print(r)

print('-'*20)

r.remove(1)#移除第一個出現的1
print(r)

print('-'*20)

r.pop(3)#移除檢索的第三項
print(r)

print('-'*20)

r.sort()#由小到大排序
print(r)

print('-'*20)

s=["zebra", "banana", "cherry","aba",'ab']
s.sort()#字母順序排序
print(s) 