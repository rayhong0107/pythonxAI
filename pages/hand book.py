import streamlit as st
with st.expander("class 1 課堂筆記"):

            
    st.write(
    """
    ## Python 基礎筆記（高中生版）

    ### 基本輸出指令

    * 使用 `print()` 來輸出資料。

    ```python
    print(1234)  # 整數
    print(1.234)  # 浮點數
    print(True)  # 布林值True
    print(False)  # 布林值False
    print("hello world")  # 字串
    ```

    ### 變數定義與使用

    * 變數可以用來儲存資料，並可重新賦值。

    ```python
    a = 10
    print(a)  # 輸出10
    a = 20
    print(a)  # 輸出20
    a = "apple"
    print(a)  # 輸出apple
    ```

    ### 數字運算

    * 基本運算符號：

    ```python
    x = 4
    x = x + 5
    print(x)  # 9
    x = x ** 4  # 指數運算，x的4次方
    print(x)
    print(x + x + 8)  # 加法
    print(x - 1)  # 減法
    print(x * 2)  # 乘法
    print(x / 2)  # 除法
    print(x // 20)  # 整除（無小數）
    print(x % 3)  # 取餘數
    print(x ** 2)  # 再次指數運算
    ```

    ### 浮點數特性

    ```python
    v1 = 0.1
    v2 = 0.2
    print(v1 + v2)  # 結果可能有精度問題，輸出約0.30000000000000004
    ```

    ### 字串處理

    * 字串可以用加法與乘法。

    ```python
    s1 = "hello"
    s2 = "world"
    print(s1 + " " + s2 * 3)  # 輸出hello worldworldworld
    ```

    ### 格式化字串

    * 可插入變數到字串中。

    ```python
    name = "python"
    age = 30
    new_str = f"我是{name}今年{age}歲"
    print(new_str)  # 我是python今年30歲
    ```

    ### 常用函式

    * 長度函式：`len()`

    ```python
    print(len(""))  # 0
    print(len("hello"))  # 5
    ```

    * 資料型態查詢：`type()`

    ```python
    print(type(True))  # 布林值
    print(type(5))  # 整數
    print(type("hello"))  # 字串
    print(type(0.5))  # 浮點數
    ```

    ### 資料型態轉換

    * 整數轉換：`int()`（字串轉整數時必須是數字字串，否則會報錯）
    * 浮點數轉換：`float()`（字串轉浮點數同樣必須是數字字串）
    * 布林值轉換：`bool()`（0、空字串為False，其餘為True）
    * 字串轉換：`str()`

    ```python
    print(int(True))  # 1
    print(int(123))  # 123

    print(float(True))  # 1.0
    print(float(123))  # 123.0

    print(bool(0))  # False
    print(bool(1))  # True
    print(bool("hello"))  # True
    print(bool(""))  # False

    print(str(True))  # "True"
    print(str(123))  # "123"
    ```

    ### 使用者輸入

    * 使用 `input()` 函式接受使用者輸入，輸入資料預設為字串。

    ```python
    c = input("請輸入你的名字：")
    print("原來是" + c + "啊！")
    ```

    * 輸入數字後需透過轉換才能做數字運算。

    ```python
    d = input("圓的半徑是多少：")
    area = 3.14 * float(d) ** 2
    print("圓的面積是" + str(area))
    ```

    ---

    ## Streamlit 基礎

    * 安裝方式：`import streamlit as st`
    * 常見指令：

    ```python
    st.title("這是標題")
    st.write("這是write寫的內容")
    st.text("這是text寫的內容")
    ```

    ### Markdown 語法展示

    * 使用 `st.markdown()` 輸出具格式的文字：

    ````python
    st.markdown(\"""
    這是用markdown寫的字串
    * **粗體文字**
    * *斜體文字*
    * [連結](https://www.example.com)
    * 程式碼
    ```python
    print("Hello, World!")
    ````

    # 標題一

    ## 標題二

    ### 標題三

    #### 標題四

    \""")

    """
    )
with st.expander("class 2 課堂筆記"):
    st.write(
    """


## ✅ 比一比（比較運算子）

就像比大小一樣，我們可以用 Python 來問問題：

```python
print(1 == 2)   # 是一樣的嗎？（False）
print(1 != 2)   # 不一樣嗎？（True）
print(1 >= 2)   # 大於或等於嗎？
print(1 <= 2)   # 小於或等於嗎？
print(1 > 2)    # 比較大？
print(1 < 2)    # 比較小？
```

---

## 🧠 想一想（邏輯運算子）

Python 也會像大腦一樣思考：

```python
print(not True)         # 不是「對」→「錯」
print(True and False)   # 兩個都對才會是對
print(True or False)    # 有一個對就算對
```

---

## 🔒 小小密碼鎖（if 判斷）

我們可以做簡單的「密碼檢查」功能：

```python
password = input("請輸入密碼:")
if password == "1234":
    print("歡迎 Ray")
elif password == "5678":
    print("歡迎 Mike")
else:
    print("密碼錯誤")
```

---

## 📅 這是閏年嗎？（閏年判斷）

```python
year = int(input("請輸入年分:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("是閏年")
else:
    print("不是閏年")
```

---

## 🧮 Streamlit 小互動（數字輸入、按鈕、動畫）

```python
import streamlit as st

# 數字輸入
number = st.number_input("請輸入一個數字", min_value=0., max_value=100., value=60., step=.1)
st.write(f"你輸入的數字是: {number}")
```

### 🎓 成績評分系統

```python
grade = st.number_input("請輸入成績", min_value=0, max_value=100, value=60, step=1)

if grade >= 90:
    st.write("你的成績為 A")
elif grade >= 80:
    st.write("你的成績為 B")
elif grade >= 70:
    st.write("你的成績為 C")
elif grade >= 60:
    st.write("你的成績為 D")
else:
    st.write("你的成績為 F")
```

---

## 🎉 按鈕動畫

```python
st.button("愛點不點", key="button1")
if st.button("愛點不點", key="button2"):
    st.balloons()  # 放氣球
if st.button("愛點不點", key="button3"):
    st.snow()      # 下雪
```

---

## 🔁 重複做（for 迴圈）

```python
for i in range(5):
    st.write("Ray")
    st.write(i)
```

---

## 🔢 迴圈更多玩法

```python
for i in range(2, 6):       # 從2到5
    st.write(i)

for i in range(2, 10, 2):   # 每次跳2
    st.write(i)
```

---

## 🏯 數字金字塔 + 小聖誕樹

````python
# 數字金字塔
number = int(st.number_input("請輸入一個數字", min_value=1, max_value=10, value=1, step=1))
a = 1
for i in range(number):
    st.write(str(a) * a)
    a += 1

# 星星聖誕樹
arrow = ""
num2 = st.number_input("請輸入一個數字", step=1, min_value=1)
for i in range(1, int(num2) + 1):
    arrow += " " * (int(num2) - i) + "*" * (2 * i - 1) + "\n"
for i in range(int(num2)):
    arrow += " " * (int(num2) - 1) + "*" + "\n"
st.write(f"```\n{arrow}```")
````

---

## 📦 神奇的串列（List）

串列就像一個裝東西的盒子，可以放很多種東西：

```python
L1 = []                         # 空的
L2 = ["蘋果"]                   # 只有一個
L3 = ["蘋果", "香蕉", "橘子"]   # 三個水果
L4 = [1, 2, 3, 4, 5]
L5 = [1, "蘋果", 3.14, True]
L6 = [1, 2, 3, ["蘋果", "香蕉"]]  # 裡面還有小盒子！

print(L6[1])        # 拿出第二個
print(L6[3][0])     # 拿出裡面盒子的第一個
```

### 🎯 切片用法

```python
L = [1, 2, 3, "a", "b", "c"]

print(L[1:4:2])  # 從第2個到第4個，每隔1個取一次
print(L[1:4])    # 從第2個到第4個
print(L[::2])    # 從頭到尾，每隔一個取
```

---

""")