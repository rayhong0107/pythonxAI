## Python 基礎筆記（高中生版）

### 基本輸出指令

- 使用 `print()` 來輸出資料。

```python
print(1234)  # 整數
print(1.234)  # 浮點數
print(True)  # 布林值True
print(False)  # 布林值False
print("hello world")  # 字串
```

### 變數定義與使用

- 變數可以用來儲存資料，並可重新賦值。

```python
a = 10
print(a)  # 輸出10
a = 20
print(a)  # 輸出20
a = "apple"
print(a)  # 輸出apple
```

### 數字運算

- 基本運算符號：

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

- 字串可以用加法與乘法。

```python
s1 = "hello"
s2 = "world"
print(s1 + " " + s2 * 3)  # 輸出hello worldworldworld
```

### 格式化字串

- 可插入變數到字串中。

```python
name = "python"
age = 30
new_str = f"我是{name}今年{age}歲"
print(new_str)  # 我是python今年30歲
```

### 常用函式

- 長度函式：`len()`

```python
print(len(""))  # 0
print(len("hello"))  # 5
```

- 資料型態查詢：`type()`

```python
print(type(True))  # 布林值
print(type(5))  # 整數
print(type("hello"))  # 字串
print(type(0.5))  # 浮點數
```

### 資料型態轉換

- 整數轉換：`int()`（字串轉整數時必須是數字字串，否則會報錯）
- 浮點數轉換：`float()`（字串轉浮點數同樣必須是數字字串）
- 布林值轉換：`bool()`（0、空字串為 False，其餘為 True）
- 字串轉換：`str()`

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

- 使用 `input()` 函式接受使用者輸入，輸入資料預設為字串。

```python
c = input("請輸入你的名字：")
print("原來是" + c + "啊！")
```

- 輸入數字後需透過轉換才能做數字運算。

```python
d = input("圓的半徑是多少：")
area = 3.14 * float(d) ** 2
print("圓的面積是" + str(area))
```

---

## Streamlit 基礎

- 安裝方式：`import streamlit as st`
- 常見指令：

```python
st.title("這是標題")
st.write("這是write寫的內容")
st.text("這是text寫的內容")
```

### Markdown 語法展示

- 使用 `st.markdown()` 輸出具格式的文字：

````python
st.markdown("""
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

""")

```

透過以上整理，可以有效理解今天學到的 Python 與 Streamlit 的基本操作與使用方式！

```
