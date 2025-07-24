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