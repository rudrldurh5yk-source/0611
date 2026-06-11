import streamlit as st
import numpy as np

st.title("🌱 스마트팜 환경 최적화 대시보드")

# 1. 제어 슬라이더
temp = st.slider("현재 온실 온도 (°C)", 15.0, 35.0, 24.0)
humidity = st.slider("현재 온실 상대습도 (%)", 20, 100, 60)

# 2. 수학 공식을 코드로 그대로 구현
vp_sat = 0.61078 * np.exp((17.27 * temp) / (temp + 237.3))
vpd = vp_sat * (1 - (humidity / 100.0))

# 3. 계산 결과 시각화
st.subheader(f"현재 계산된 VPD(증기압차): {vpd:.2f} kPa")

if 0.8 <= vpd <= 1.2:
    st.success("🎯 식물 성장에 완벽한 최적 환경입니다!")
elif vpd < 0.8:
    st.warning("💦 너무 습합니다. 환풍기를 가동하거나 제습이 필요합니다.")
else:
    st.error("🔥 너무 건조합니다. 기공이 닫히고 있으니 가습기를 켜세요.")
