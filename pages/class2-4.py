import streamlit as st
number = int(st.number_input("請輸入一個數字", min_value=1, max_value=10, value=1, step=1))
a=1
st.write('數字金字塔')
for i in range(number):
    st.write(str(a) *a)
    a=a+1

arrow=""
num2= st.number_input("請輸入一個數字", step=1,min_value=1)
for i in range(1, num2 + 1):
    arrow=arrow + (" " * (num2 - i) + "*" * (2 * i - 1)+ "\n")
for i in range(num2):
    arrow= arrow+ (" " *(num2-1) + "*" + "\n") 
st.write(f"```\n{arrow}```")