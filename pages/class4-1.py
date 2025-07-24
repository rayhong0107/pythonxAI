
D1 = {}
D2 = {"apple":"蘋果"}
D3 = {1: "one", 2:"two", 3:"three", "三": "three"}

print(D2["apple"])
print(D3[2])
print(D3["三"])

for key in D3:
    print(key)

print('-'*20)

for key in D3.keys():
    print(key)

print('-'*20)

for value in D3.values():
    print(value)

print('-'*20)

for key, value in D3.items():
    print(key, value)   

print('-'*20)

D3[2]='二'
print(D3)
print('-'*20)
D3[4]='four'
print(D3)
print('-'*20)
v= D3.pop(1)
print(f'刪除的值, {v}')
print(D3)
print('-'*20)
v= D3.pop(5,'not found')
print(D3)
print(f'刪除的值{v}')
print('D3的長度', len(D3))

print('-'*20)

print(1 in D3)
print(2 in D3)
print('three' in D3)

print('-'*20)

friuts=['apple','banana','orange']
print('banana' in friuts)
print('grape' in friuts)