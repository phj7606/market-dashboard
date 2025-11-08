import streamlit as st
import yfinance as yf
import datetime

st.title("Streamlit + yfinance 최소 재현 테스트")

st.write("현재 시간:", datetime.datetime.now())

try:
    df = yf.download('^GSPC', period='5d', interval='1d')
    st.write("yfinance 데이터:")
    st.write(df)
    if df.empty:
        st.error("yfinance로 받아온 데이터가 비어 있습니다.")
    else:
        st.success("yfinance 데이터가 정상적으로 받아졌습니다!")
except Exception as e:
    st.error(f"yfinance 에러: {e}") 