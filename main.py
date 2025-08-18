import streamlit as st

# 페이지 설정 🎉
st.set_page_config(page_title="MBTI 진로 추천 🎭✨", page_icon="🌈", layout="centered")

# 헤더 🌟
st.markdown(
    """
    <h1 style="text-align:center; font-size:50px; color:#FF6F91;">
    🌈 MBTI 기반 직업 추천 💼✨
    </h1>
    <h3 style="text-align:center; color:#6A0572;">
    나의 성격유형(MBTI)에 맞는 멋진 직업을 찾아보자! 🚀
    </h3>
    """, unsafe_allow_html=True
)

# MBTI 목록 📌
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 직업 추천 사전 📚
job_dict = {
    "INTJ": "🧠 전략가 → 데이터 과학자, 경영 컨설턴트, 연구원",
    "INTP": "🔍 탐구자 → 철학자, 발명가, 프로그래머",
    "ENTJ": "👑 리더 → 기업가, 변호사, CEO",
    "ENTP": "💡 아이디어 뱅크 → 방송인, 창업가, 마케팅 전문가",
    "INFJ": "🌌 선지자 → 상담가, 심리학자, 인권운동가",
    "INFP": "🎨 꿈꾸는 이상주의자 → 작가, 예술가, 교사",
    "ENFJ": "🤝 정의로운 지도자 → 교사, 사회운동가, HR 전문가",
    "ENFP": "🔥 열정적인 활동가 → 광고 기획자, 방송 작가, 여행 크리에이터",
    "ISTJ": "📊 꼼꼼한 관리자 → 회계사, 공무원, 군인",
    "ISFJ": "💖 따뜻한 수호자 → 간호사, 교사, 사회복지사",
    "ESTJ": "🏢 체계적인 조직가 → 관리자, 경찰관, 판사",
    "ESFJ": "🌸 친절한 협력가 → 간호사, 교사, 이벤트 플래너",
    "ISTP": "⚙️ 실용적 장인 → 엔지니어, 파일럿, 메카닉",
    "ISFP": "🎶 자유로운 영혼 → 디자이너, 음악가, 요리사",
    "ESTP": "🏎️ 모험가 → 기업가, 스포츠 선수, 세일즈 전문가",
    "ESFP": "🎤 무대의 스타 → 배우, 가수, 엔터테이너"
}

# MBTI 선택 ✨
st.markdown("## 👉 당신의 MBTI를 선택해주세요 💖")
selected_mbti = st.selectbox("📌 MBTI 선택하기", mbti_list)

# 결과 출력 🎉
if selected_mbti:
    st.markdown(
        f"""
        <div style="text-align:center; font-size:25px; background-color:#FFE4E1; 
        padding:20px; border-radius:20px; box-shadow:2px 2px 10px #FFB6C1;">
        ✨ 당신의 MBTI는 <b style="color:#FF1493;">{selected_mbti}</b> ✨  
        <br><br>
        👉 추천 직업은...  
        <h2 style="color:#6A0572;">{job_dict[selected_mbti]}</h2> 🚀🌟
        </div>
        """, unsafe_allow_html=True
    )

# 푸터 🎇
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>Made with ❤️ by Career Explorer 🌍✨</p>", 
    unsafe_allow_html=True
)
