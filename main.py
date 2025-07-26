import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(
    page_title="발리 힐링 여행 코스 추천",
    page_icon="🌴",
    layout="wide",
)

st.title('🇮🇩 7월 말, 발리 힐링 여행 코스 추천')

st.write("""
7월의 발리는 건기에 속해 여행하기 가장 좋은 시기입니다. 쾌적한 날씨 속에서 발리의 아름다운 자연과 문화를 만끽해 보세요.
아래 추천 코스는 발리의 핵심 지역을 둘러보며 휴양과 관광을 모두 즐길 수 있도록 구성했습니다.
""")

# 여행지 위치
locations = {
    '스미냑 비치': [-8.6917, 115.1583], '짱구 비치': [-8.6593, 115.1385],
    '우붓 왕궁': [-8.5069, 115.2624], '우붓 시장': [-8.5076, 115.2622],
    '몽키 포레스트': [-8.5193, 115.2592], '렘푸양 사원': [-8.3902, 115.6321],
    '띠르따 강가': [-8.4120, 115.5902], '뜨갈랄랑': [-8.4312, 115.2779],
    '울루와뚜 사원': [-8.8291, 115.0849], '짐바란 베이': [-8.7844, 115.1637],
    '꾸따 비치': [-8.7186, 115.1685]
}

restaurants = {
    'The Shady Shack (짱구)': {'lat': -8.6635, 'lon': 115.1363, 'desc': '건강한 채식/비건 메뉴'},
    'La Favela (스미냑)': {'lat': -8.6800, 'lon': 115.1561, 'desc': '독특한 인테리어의 바 & 레스토랑'},
    "Naughty Nuri's Warung (우붓)": {'lat': -8.4975, 'lon': 115.2559, 'desc': '인생 폭립을 맛볼 수 있는 곳'},
    'Warung Babi Guling Ibu Oka (우붓)': {'lat': -8.5064, 'lon': 115.2621, 'desc': '발리 전통 새끼돼지 통구이'},
    'Sari Organik (우붓)': {'lat': -8.4950, 'lon': 115.2592, 'desc': '논밭 뷰의 유기농 레스토랑'},
    'Jimbaran Bay Seafood (짐바란)': {'lat': -8.7779, 'lon': 115.1676, 'desc': '해변에서의 로맨틱한 해산물 BBQ'},
    'Bumbu Bali 1 (누사두아)': {'lat': -8.7958, 'lon': 115.2229, 'desc': '정통 발리 요리 전문점'},
    'Fat Chow (꾸따)': {'lat': -8.7159, 'lon': 115.1712, 'desc': '맛있는 아시안 퓨전 요리'}
}

# 병원 정보 추가
hospitals = {
    "BIMC Hospital Kuta": {
        "lat": -8.7167,
        "lon": 115.1783,
        "address": "Jl. By Pass Ngurah Rai No.100X, Kuta, Bali",
        "phone": "+62 361 761263"
    },
    "Siloam Hospitals Denpasar": {
        "lat": -8.6723,
        "lon": 115.2176,
        "address": "Jl. Sunset Road No.818, Denpasar, Bali",
        "phone": "+62 361 779900"
    },
    "Rumah Sakit Umum Sanglah": {
        "lat": -8.6694,
        "lon": 115.2190,
        "address": "Jl. Diponegoro, Denpasar, Bali",
        "phone": "+62 361 227911"
    }
}

tab1, tab2, tab3 = st.tabs(["🗺️ 여행 지도", "🗓️ 세부 일정", "🍽️ 맛집 리스트"])

with tab1:
    st.header("📍 여행지 + 맛집 + 병원 지도")

    m = folium.Map(location=[-8.5, 115.2], zoom_start=10)

    # 여행지 마커
    for name, coords in locations.items():
        folium.Marker(
            location=coords,
            popup=name,
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)

    # 맛집 마커
    for name, info in restaurants.items():
        folium.Marker(
            location=[info['lat'], info['lon']],
            popup=f"{name}<br>{info['desc']}",
            icon=folium.Icon(color='green', icon='cutlery')
        ).add_to(m)

    # 병원 마커
    for name, info in hospitals.items():
        folium.Marker(
            location=[info['lat'], info['lon']],
            popup=f"<b>{name}</b><br>{info['address']}<br>📞 {info['phone']}",
            icon=folium.Icon(color='red', icon='plus-sign')
        ).add_to(m)

    st_data = st_folium(m, width=1200, height=600)

# tab2, tab3 그대로 유지 (복사 붙여넣기 가능 — 길어서 생략)
