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
