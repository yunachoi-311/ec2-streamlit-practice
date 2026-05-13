import streamlit as st

st.title("EC2 Streamlit 배포 실습")

st.write("안녕하세요! EC2에서 실행 중인 Streamlit 앱입니다.")

name = st.text_input("이름을 입력하세요")

if st.button("확인"):
    st.success(f"{name}님, EC2 배포 성공입니다!")