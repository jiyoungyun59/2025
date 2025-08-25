import streamlit as st
import random

# --- 따뜻하고 벅차오르는 문구 데이터 ---
quotes = {
    "행복 😊": [
        "너의 오늘은 어제보다 더 빛나고 있어 ✨",
        "세상이 너를 중심으로 반짝이고 있어 🌈",
        "작은 기쁨이 모여 너의 삶을 환하게 밝히고 있어 🌞"
    ],
    "슬픔 😢": [
        "너의 눈물이 의미 없는 건 하나도 없어 💧",
        "세상은 네가 다시 웃을 날을 기다리고 있어 🌷",
        "지금의 슬픔은 너를 더 단단하게 만들어줄 거야 🌙"
    ],
    "불안 😟": [
        "너는 이미 충분히 잘하고 있어 🌊",
        "걱정은 결국 사라지고, 네가 빛나는 순간만 남을 거야 🌟",
        "너의 발걸음은 천천히지만 확실하게 앞으로 나아가고 있어 🚶‍♂️"
    ],
    "설렘 💖": [
        "너의 두근거림은 새로운 시작의 신호야 🌸",
        "가슴 뛰는 순간이 네 인생을 가장 아름답게 만들어 🌈",
        "설레는 마음이 널 더 빛나게 하고 있어 ✨"
    ],
    "분노 🔥": [
        "네 안의 불꽃은 세상을 바꿀 힘이야 🔥",
        "화는 사라지지만, 너의 열정은 남아 세상을 밝힐 거야 ☀️",
        "너의 뜨거움은 결국 위대한 힘으로 바뀔 거야 ⚡"
    ]
}

# --- 앱 UI ---
st.set_page_config(page_title="기분별 위로의 한마디", page_icon="🌟", layout="centered")

st.markdown(
    """
    <h1 style="text-align:center; color:#ff66b2; font-size:60px;">
        🌟 오늘의 마음 위로 한마디 🌟
    </h1>
    """,
    unsafe_allow_html=True
)

# 기분 선택
emotion = st.selectbox("지금 너의 기분은 어떤가요? 💭", list(quotes.keys()))

# 버튼 클릭 시 문구 출력
if st.button("✨ 위로 받기 ✨"):
    chosen_quote = random.choice(quotes[emotion])
    
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #ffb3d9, #ffe066, #a3e6ff);
            padding: 40px;
            border-radius: 25px;
            box-shadow: 0px 8px 30px rgba(0,0,0,0.3);
            text-align: center;
        ">
            <h2 style="color:#ffffff; font-size:36px; line-height:1.6;">
                {chosen_quote}
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.balloons()
    st.snow()
