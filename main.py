import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# --- 페이지 설정 ---
st.set_page_config(
    page_title="발리 힐링 여행 코스 추천",
    page_icon="🌴",
    layout="wide",
)

# --- 제목 및 설명 ---
st.title("🇮🇩 7월 말, 발리 힐링 여행 코스 추천")
st.write("""
7월의 발리는 건기에 속해 여행하기 가장 좋은 시기입니다. 쾌적한 날씨 속에서 발리의 아름다운 자연과 문화를 만끽해 보세요.
아래 추천 코스는 발리의 핵심 지역을 둘러보며 휴양과 관광을 모두 즐길 수 있도록 구성했습니다.
""")

# --- 장소 데이터 ---
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

hospitals = {
    "BIMC Hospital Kuta": {
        "lat": -8.7167,
        "lon": 115.1783,
        "address": "Jl. By Pass Ngurah Rai No.100X, Kuta, Bali",
        "phone": "+62 361 761263",
        "foreigner_friendly": True
    },
    "Siloam Hospitals Denpasar": {
        "lat": -8.6723,
        "lon": 115.2176,
        "address": "Jl. Sunset Road No.818, Denpasar, Bali",
        "phone": "+62 361 779900",
        "foreigner_friendly": True
    },
    "Rumah Sakit Umum Sanglah": {
        "lat": -8.6694,
        "lon": 115.2190,
        "address": "Jl. Diponegoro, Denpasar, Bali",
        "phone": "+62 361 227911",
        "foreigner_friendly": False
    }
}

# --- 탭 UI 구성 ---
tab1, tab2, tab3 = st.tabs(["🗺️ 여행 지도", "🗓️ 세부 일정", "🍽️ 맛집 리스트"])

# --- 지도 탭 ---
with tab1:
    st.header("📍 여행지 + 맛집 + 병원 지도")

    selected_spot = st.selectbox(
        "🗓️ 세부 일정 중 관심 장소를 선택하면 지도에서 위치를 확인할 수 있어요.",
        list(locations.keys()) + list(restaurants.keys())
    )

    # 지도 중심 위치 계산
    center = None
    if selected_spot in locations:
        center = locations[selected_spot]
    elif selected_spot in restaurants:
        center = [restaurants[selected_spot]["lat"], restaurants[selected_spot]["lon"]]

    # 지도 생성
    m = folium.Map(location=center if center else [-8.5, 115.2], zoom_start=13 if center else 10)

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
        popup_html = (
            f"<b>{name}</b><br>"
            f"{info['address']}<br>📞 {info['phone']}<br>"
            f"🌐 외국인 진료 가능: {'✅' if info['foreigner_friendly'] else '❌'}"
        )
        folium.Marker(
            location=[info['lat'], info['lon']],
            popup=popup_html,
            icon=folium.Icon(color='red', icon='plus-sign')
        ).add_to(m)

    # 선택된 장소 강조 마커
    if center:
        folium.Marker(
            location=center,
            popup=f"<b>{selected_spot}</b>",
            icon=folium.Icon(color='orange', icon='star')
        ).add_to(m)

    st_data = st_folium(m, width=1200, height=600)

# --- 일정 탭 ---
with tab2:
    st.header("🗓️ 4박 5일 세부 추천 일정")

    with st.expander("**Day 1: 스미냑/짱구 - 활기찬 해변과 트렌디한 감성**", expanded=True):
        st.markdown("""
        - **오후**: 공항 도착 후 스미냑 또는 짱구 숙소 이동
        - **저녁**: 해변 레스토랑 또는 비치 클럽 방문
        - **주요 스팟**: 스미냑 비치, 짱구 비치, 포테이토 헤드 클럽
        """)

    with st.expander("**Day 2: 우붓 - 발리의 예술과 영혼을 만나다**"):
        st.markdown("""
        - **오전**: 우붓 이동, 문화탐방
        - **오후**: 우붓 왕궁, 우붓 시장, 몽키 포레스트 탐방
        """)

    with st.expander("**Day 3: 우붓 근교 자연 탐험**"):
        st.markdown("""
        - **오전**: 렘푸양 사원 방문 (천국의 문)
        - **오후**: 띠르따 강가, 뜨갈랄랑 계단식 논 방문
        """)

    with st.expander("**Day 4: 울루와뚜 / 짐바란**"):
        st.markdown("""
        - **오후**: 울루와뚜 사원 절벽뷰 감상
        - **저녁**: 케착 댄스 공연 → 짐바란 해변 해산물 BBQ
        """)

    with st.expander("**Day 5: 꾸따 및 출국**"):
        st.markdown("""
        - **오전**: 꾸따 비치 산책, 쇼핑
        - **오후**: 공항 이동 및 출국
        """)

# --- 맛집 탭 ---
with tab3:
    st.header("🍽️ 지역별 추천 맛집")

    st.subheader("🌴 스미냑 / 짱구")
    st.text("La Favela: 신비로운 정글 컨셉의 바 & 레스토랑")
    st.text("The Shady Shack: 건강한 채식 요리")

    st.subheader("🌳 우붓")
    st.text("Naughty Nuri's Warung: 부드러운 폭립")
    st.text("Warung Babi Guling Ibu Oka: 전통 바비굴링")
    st.text("Sari Organik: 논밭 뷰 유기농 레스토랑")

    st.subheader("🌊 짐바란 / 울루와뚜")
    st.text("Jimbaran Bay Seafood: 바닷가 BBQ")
    st.text("Bumbu Bali 1: 정통 발리 요리")

    st.subheader("☀️ 꾸따")
    st.text("Fat Chow: 트렌디한 아시안 퓨전 요리")

    st.info("💡 Grab / Gojek 앱으로 지역 간 이동이 편리합니다.")
