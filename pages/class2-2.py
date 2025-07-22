import streamlit as st
number= st.number_input("請輸入一個數字", min_value=0., max_value=100., value=60., step=.1)
st.write(f"你輸入的數字是: {number}")

grade = st.number_input("請輸入成績", min_value=0, max_value=100, value=60, step=1)
# st.write(f"你的成績為:", if grade>=60 and grade<70:
#          "D"
#          elif grade>=70 and grade<80:
#             "C"
#             elif grade>=80 and grade<90:
#               "B"  
#               elif grade>=90 and grade<=100:
#               "A"
#                 else:
#                       "F"  )
if grade>=60 and grade<70:
    st.write("你的成績為D")
elif grade>=70 and grade<80:
    st.write("你的成績為C")
elif grade>=80 and grade<90:
    st.write("你的成績為B") 
elif grade>=90 and grade<=100:
    st.write("你的成績為A")
else:
    st.write("你的成績為F") 


st.button("愛點不點", key="button1")
if st.button("愛點不點", key="button2"):
    st.balloons()
if st.button("愛點不點", key="button3"):
    st.snow()

for i in range(5):
    st.write("ray")
    st.write(i)