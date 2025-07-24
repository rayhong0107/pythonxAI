def hello():
    print("hello"*20)
hello()

def hello(name):
    print("hello "+name)
hello("ray")

def my_max(a,b):
    if a>b:
        return a
    else:
        return b

def calculate_circle_area(r,pi=3.14,scale=1):
    return (r*scale)**2 *pi

hello("mike")

print(my_max(100000,66666666))
print(calculate_circle_area(10000000))
print(calculate_circle_area(100,scale=10))

print("-"*20)

area=123

length=5
def calculate_square__area():
    # print('面積是',area)#會報錯
    area=length**2
    print("面積是", area)

def calculate_square__area2():
    global area
    area=length**2

def calculate_square__area3():
    area=length**2
    return area

length=10 
calculate_square__area()
calculate_square__area2()
print(calculate_square__area3())
print("面積是", area)


a=int(input())
b=int(input())
c=int(input())
d=int(input())
def distance(x1,y1,x2,y2):
    e=(x1-x2)**2+(y1-y2)**2
    e=e**0.5
    return e
print(distance(a,b,c,d))

