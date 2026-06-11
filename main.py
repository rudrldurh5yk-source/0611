import streamlit as st
import pandas as pd
import numpy as np

st.title("🥬 전국 배추 최적 재배지 선정 시스템")

# 1. 생명과학 + 수학: 배추 적합도 점수 계산 함수 (수학 조의 결과물)
def calculate_cabbage_score(temp, humidity, solar):
    # 기온 점수: 19도에서 만점(100), 멀어질수록 감점되는 이차함수 모델
    temp_score = max(0, 100 - 4 * ((temp - 19) ** 2))
    
    # 습도 점수: 60~80% 사이가 좋음
    if 60 <= humidity <= 80:
        humid_score = 100
    else:
        humid_score = max(0, 100 - abs(humidity - 70))
        
    # 최종 가중치 합산 (기온이 가장 중요하다고 가정)
    final_score = (temp_score * 0.5) + (humid_score * 0.3) + (solar * 0.2)
    return final_score

# 2. 가상의 전국 날씨 데이터 (실제 수업에선 기상청 CSV 파일을 pd.read_csv로 로드)
weather_data = pd.DataFrame({
    '지역': ['강원 대관령', '전남 해남', '서울', '제주도'],
    '평균기온(°C)': [16.5, 23.0, 21.5, 24.5],
    '상대습도(%)': [75, 80, 60, 85],
    '일사량지수': [90, 85, 70, 95] # 물리학/수학적으로 정규화한 값
})

st.subheader("📍 전국 주요 지역 기상 데이터 (가을철 기준)")
st.dataframe(weather_data)

# 3. 데이터 분석 및 점수 매칭
scores = []
for idx, row in weather_data.iterrows():
    score = calculate_cabbage_score(row['평균기온(°C)'], row['상대습도(%)'], row['일사량지수'])
    scores.append(score)

weather_data['배추 적합도 점수'] = scores
weather_data = weather_data.sort_values(by='배추 적합도 점수', ascending=False)

# 4. Streamlit 시각화
st.subheader("🏆 배추 재배 최적의 지역 순위")
st.bar_chart(data=weather_data, x='지역', y='배추 적합도 점수')

best_region = weather_data.iloc[0]['지역']
st.success(s"📊 분석 결과, 우리나라에서 배추를 키우기에 가장 좋은 지역은 **[{best_region}]** 입니다!")
