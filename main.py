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
with tab2:
    st.header("🗓️ 4박 5일 세부 추천 일정")

    # 아코디언 형태로 일정 제공
    with st.expander("**Day 1: 스미냑/짱구 - 활기찬 해변과 트렌디한 감성**", expanded=True):
        st.markdown("""
        - **오후**: 응우라라이 국제공항 도착 후, 스미냑 또는 짱구 지역의 숙소로 이동합니다.
        - **저녁**: 해변에 위치한 레스토랑이나 비치 클럽에서 발리의 첫날밤을 즐겨보세요. 서핑으로 유명한 곳인 만큼, 해변의 활기찬 분위기를 느낄 수 있습니다.
        - **주요 스팟**: 스미냑 비치, 짱구 비치, 포테이토 헤드 비치 클럽
        """)

    with st.expander("**Day 2: 우붓 - 발리의 예술과 영혼을 만나다**"):
        st.markdown("""
        - **오전**: 발리의 문화 중심지, 우붓으로 이동합니다.
        - **오후**: 우붓 왕궁과 활기 넘치는 우붓 시장을 둘러보며 현지 공예품을 구경하세요. 그 후, 긴꼬리원숭이들이 자유롭게 살아가는 몽키 포레스트를 방문합니다.
        - **주요 스팟**: 우붓 왕궁, 우붓 시장, 몽키 포레스트
        """)

    with st.expander("**Day 3: 우붓 근교 - 인생 사진과 함께하는 자연 탐험**"):
        st.markdown("""
        - **오전**: '천국의 문'으로 유명한 렘푸양 사원으로 떠납니다. 아궁 화산을 배경으로 멋진 사진을 남겨보세요. (대기 시간이 길 수 있으니 아침 일찍 출발하는 것을 추천합니다.)
        - **오후**: 옛 발리 왕족의 휴양지였던 물의 궁전, 띠르따 강가를 산책하고, 대표적인 포토 스팟인 뜨갈랄랑 계단식 논을 방문합니다.
        - **주요 스팟**: 렘푸양 사원, 띠르따 강가, 뜨갈랄랑
        """)

    with st.expander("**Day 4: 울루와뚜/짐바란 - 장엄한 절벽과 로맨틱한 일몰**"):
        st.markdown("""
        - **오후**: 발리 남쪽의 울루와뚜 절벽 사원으로 이동하여 인도양의 탁 트인 절경을 감상합니다.
        - **저녁**: 해질녘에 맞춰 발리 전통 공연인 케착 파이어 댄스를 관람하고, 짐바란 해변으로 이동해 갓 잡은 신선한 해산물로 로맨틱한 저녁 식사를 즐깁니다.
        - **주요 스팟**: 울루와뚜 사원, 짐바란 베이
        """)

    with st.expander("**Day 5: 출국 - 마지막 여운 즐기기**"):
        st.markdown("""
        - **오전**: 비행기 시간에 맞춰 꾸따 비치 근처의 쇼핑몰이나 스미냑 거리에서 마지막 쇼핑을 즐깁니다.
        - **오후**: 공항으로 이동하여 아쉬운 발리 여행을 마무리합니다.
        - **주요 스팟**: 꾸따 비치, 비치워크 쇼핑센터
        """)


with tab3:
    st.header("🍽️ 지역별 추천 맛집")
    st.write("여행 코스에 맞춰 방문하기 좋은 검증된 맛집 리스트입니다.")

    st.subheader("🌴 스미냑 / 짱구")
    st.text("La Favela: 신비로운 정글 컨셉의 인테리어가 인상적인 곳")
    st.text("The Shady Shack: 건강하고 맛있는 채식 요리를 즐길 수 있는 곳")

    st.subheader("🌳 우붓")
    st.text("Naughty Nuri's Warung: 부드러운 폭립과 특제 소스의 환상적인 조화")
    st.text("Warung Babi Guling Ibu Oka: 발리 전통 음식 '바비굴링'의 정석")
    st.text("Sari Organik: 아름다운 논밭을 바라보며 즐기는 힐링 푸드")

    st.subheader("🌊 짐바란 / 울루와뚜")
    st.text("Jimbaran Bay Seafood: 해변의 노을을 보며 즐기는 낭만적인 해산물 BBQ")
    st.text("Bumbu Bali 1: 인도네시아의 다양한 향신료를 경험할 수 있는 정통 발리 요리")

    st.subheader("☀️ 꾸따")
    st.text("Fat Chow: 다양한 아시안 퓨전 음식을 맛볼 수 있는 트렌디한 맛집")

    st.info("💡 **여행 Tip**: 발리 내에서 지역 간 이동은 '그랩(Grab)'이나 '고젝(Gojek)' 같은 차량 호출 앱을 이용하면 편리합니다. 또는 전일 차량을 대절하여 원하는 코스대로 자유롭게 여행하는 것도 좋은 방법입니다.")
