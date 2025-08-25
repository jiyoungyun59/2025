import streamlit as st
import random

# 감정 키워드별 따뜻한 말과 노래 추천
emotion_data = {
    "슬픔": {
        "message": [
            "지금 느끼는 아픔도 언젠가는 당신의 강함이 될 거예요 🌷",
            "눈물이 난다는 건 그만큼 진심으로 살아가고 있다는 증거예요 💧",
            "당신은 혼자가 아니에요. 이 순간도 곧 지나갈 거예요 ☀️"
        ],
        "songs": [
            ("아이유 - 너의 의미", "https://youtu.be/9GKG4AgF6eU"),
            ("Coldplay - Fix You", "https://youtu.be/k4V3Mo61fJM"),
            ("볼빨간사춘기 - 우주를 줄게", "https://youtu.be/nM0xDI5R50E")
        ]
    },
    "기쁨": {
        "message": [
            "당신의 웃음은 세상을 더 빛나게 해요 ✨",
            "행복한 지금, 그 마음을 오래오래 간직하세요 🌈",
            "당신이 웃을 때 세상도 함께 웃는 것 같아요 😄"
        ],
        "songs": [
            ("Pharrell Williams - Happy", "https://youtu.be/ZbZSe6N_BXs"),
            ("BTS - Dynamite", "https://youtu.be/gdZLi9oWNZg"),
            ("Red Velvet - 행복", "https://youtu.be/QpAn9ryoB4Y")
        ]
    },
    "불안": {
        "message": [
            "숨을 크게 들이마시고 내쉬어 보세요. 모든 게 괜찮아질 거예요 🍀",
            "당신은 지금 충분히 잘하고 있어요 🙌",
            "완벽하지 않아도 괜찮아요. 있는 그대로의 당신이 소중해요 💖"
        ],
        "songs": [
            ("Shawn Mendes - In My Blood", "https://youtu.be/36tggrpRoTI"),
            ("잔나비 - 주저하는 연인들을 위해", "https://youtu.be/bMt47wvK6u0"),
            ("폴킴 - 모든 날, 모든 순간", "https://youtu.be/OMTizJemHO8")
        ]
    },
    "분노": {
        "message": [
            "화난 마음도 결국 지나가요. 당신은 그 이상으로 강한 사람이에요 🔥",
            "잠시 숨을 고르고, 스스로를 위로해 주세요 🌌",
            "당신의 감정은 언제나 존중받을 자격이 있어요 💪"
        ],
        "songs": [
            ("Eminem - Lose Yourself", "https://youtu.be/_Yhyp-_hX2s"),
            ("Imagine Dragons - Believer", "https://youtu.be/7wtfhZwyrcc"),
            ("Stray Kids - MANIAC", "https://youtu.be/OvioeS1ZZ7o")
        ]
    }
}

st.set_page_config(page_title="감정 힐링 웹앱 💖", page_icon="🌸", layout="centered")

st.title("🌷 감정 힐링🎶")
st.write("지금 느끼는 감정을 입력해보세요. 당신만을 위한 따뜻한 말과 노래를 추천해드릴게요 💕")

# 사용자 입력
user_emotion = st.text_input("오늘 당신의 감정을 적어주세요 ✍️ (예: 슬픔, 기쁨, 불안, 분노)")

if user_emotion:
    if user_emotion in emotion_data:
        data = emotion_data[user_emotion]
        message = random.choice(data["message"])
        song = random.choice(data["songs"])

        st.markdown(f"### 💌 따뜻한 말")
        st.success(message)

        st.markdown(f"### 🎶 추천 노래")
        st.markdown(f"**{song[0]}** [👉 바로 듣기]({song[1]})")
    else:
        st.warning("앗, 아직 그 감정은 준비되지 않았어요 😢 슬픔, 기쁨, 불안, 분노 중에서 입력해보세요!")
