## Python 課堂筆記（Class 4 系列）

---

### 1. 字典（Dictionary）的基本操作

字典就是一種可以讓你用「關鍵字」來找「對應內容」的資料型態，像這樣：

```python
D1 = {}  # 空字典
D2 = {"apple": "蘋果"}
D3 = {1: "one", 2: "two", 3: "three", "三": "three"}
```

常用操作如下：

```python
print(D2["apple"])      # 印出 '蘋果'
print(D3[2])            # 印出 'two'
print(D3["三"])         # 印出 'three'
```

#### 遍歷字典

```python
for key in D3:  # 逐個拿出 key
    print(key)
```

```python
for key in D3.keys():   # 只拿 key
    print(key)
```

```python
for value in D3.values():   # 只拿 value
    print(value)
```

```python
for key, value in D3.items():  # 同時拿 key 跟 value
    print(key, value)
```

#### 新增、修改、刪除

```python
D3[2] = "二"   # 修改 key=2 的值
D3[4] = "four" # 新增 key=4 的值

v = D3.pop(1)   # 刪除 key=1，v 會存它原本的值
print(f'刪除的值, {v}')
v = D3.pop(5, 'not found')  # 刪除 key=5，如果沒有就回傳 'not found'
print(f'刪除的值{v}')
```

#### 其他小技巧

```python
print('D3的長度', len(D3))  # 字典裡有幾個 key

print(1 in D3)              # 檢查 1 是不是 key
print(2 in D3)
print('three' in D3)        # 'three' 不是 key，是 value

fruits = ['apple', 'banana', 'orange']
print('banana' in fruits)   # True
print('grape' in fruits)    # False
```

---

### 2. 顯示圖片 & Streamlit 基本操作

**顯示資料夾內所有圖片，還能調整圖片大小**

```python
import streamlit as st
import os

file_path = "image"
files = os.listdir(file_path)
st.write(files)
image_size = st.number_input("圖片大小", min_value=50, max_value=500, value=300, step=10)

for img in files:
    st.image(f'{file_path}/{img}', width=image_size)
```

- 這段會把資料夾裡的圖片全部顯示出來
- 可以調整圖片大小

---

### 3. 購物平台小專案（商品展示、購買、補貨）

這是一個簡單的線上商店功能，主要練習**資料結構操作**和**Streamlit 實作**。

- 初始化商品資料（用圖片檔名當商品名）
- 商品顯示（含價格/庫存/圖片/購買按鈕）
- 買東西會扣庫存
- 新增庫存功能

關鍵程式片段（簡化版）：

```python
if "products" not in st.session_state:
    st.session_state.products = {}

# 假設已經有圖片 files
for img in files:
    pname = img[:-4]
    if pname not in st.session_state.products:
        st.session_state.products[pname] = {'image': f'{file_path}/{img}', "price": 10, "stock": 10}

for name, detail in st.session_state.products.items():
    # 顯示圖片、名稱、價格、庫存、購買按鈕
    pass  # 省略細節

# 新增庫存
if st.button("新增庫存"):
    st.session_state.products[selected_products]["stock"] += add_number
```

- 重點：如何**操作字典**來更新、查詢商品資料。

---

### 4. 函式（Function）與區域變數、全域變數

#### 什麼是函式？

就是一段可以重複利用的程式區塊，可以有參數跟回傳值。

```python
def hello():
    print("hello" * 20)
hello()

def hello(name):
    print("hello " + name)
hello("ray")
```

#### 函式的回傳值

```python
def my_max(a, b):
    if a > b:
        return a
    else:
        return b

print(my_max(100000, 66666666))
```

#### 預設參數

```python
def calculate_circle_area(r, pi=3.14, scale=1):
    return (r*scale) ** 2 * pi
print(calculate_circle_area(100))
print(calculate_circle_area(100, scale=10))
```

#### 區域變數 & 全域變數

- 區域變數：只在函式內有用
- 全域變數：整個程式都能用，要 `global` 宣告

```python
area = 123
length = 5

def calculate_square__area():
    # area=length**2 只會影響這個函式裡的 area
    pass

def calculate_square__area2():
    global area
    area = length ** 2
```

#### 練習：計算兩點距離

```python
def distance(x1, y1, x2, y2):
    e = (x1 - x2) ** 2 + (y1 - y2) ** 2
    e = e ** 0.5
    return e
```

---

### 5. 擲骰子小遊戲（隨機數）

```python
import random

t = int(input())  # 擲骰子次數
f = []
def roll_dice(t):
    global f
    for i in range(t):
        w = random.randint(1, 6)
        f.append(w)
roll_dice(t)
print(f)

# 統計各點數出現次數
n1 = n2 = n3 = n4 = n5 = n6 = 0
for num in f:
    if num == 1: n1 += 1
    elif num == 2: n2 += 1
    elif num == 3: n3 += 1
    elif num == 4: n4 += 1
    elif num == 5: n5 += 1
    else: n6 += 1

print("1出現", n1, "次")
print("2出現", n2, "次")
# ...依此類推
```

- 重點：如何用 `random` 產生隨機數，如何計數。

---

## 小結

這次重點練到：

- 字典（Dictionary）常見操作
- 如何用 Streamlit 做互動式網頁
- 函式的寫法（含參數、回傳值、變數作用範圍）
- 利用 `random` 做小遊戲、計算統計
