import streamlit as st
import random

# 감정별 메시지와 노래 추천
emotion_data = {
    "슬픔": {
        "messages": [
            "눈물이 흐르는 건 마음이 살아있다는 증거예요 💧",
            "어둠 속에서도 반드시 새벽은 와요 🌅",
            "당신은 혼자가 아니에요. 지금 이 순간도 지나갈 거예요 🌷"
        ],
        "songs": [
            ("아이유 - 너의 의미", "https://youtu.be/9GKG4AgF6eU"),
            ("Coldplay - Fix You", "https://youtu.be/k4V3Mo61fJM")
        ]
    },
    "행복": {
        "messages": [
            "당신의 웃음이 세상을 환하게 밝히고 있어요 ✨",
            "오늘의 행복을 마음껏 만끽하세요 🌈",
            "당신이 웃는 순간, 세상도 함께 웃는 것 같아요 😄"
        ],
        "songs": [
            ("Pharrell Williams - Happy", "https://youtu.be/ZbZSe6N_BXs"),
            ("BTS - Dynamite", "https://youtu.be/gdZLi9oWNZg")
        ]
    },
    "불안": {
        "messages": [
            "심장은 두려움이 아니라 가능성 때문에 뛰는 거예요 ❤️",
            "당신은 충분히 잘하고 있어요 🙌",
            "완벽하지 않아도 괜찮아요. 있는 그대로의 당신이 소중해요 💖"
        ],
        "songs": [
            ("Shawn Mendes - In My Blood", "https://youtu.be/36tggrpRoTI")
        ]
    },
    "분노": {
        "messages": [
            "화난 마음도 결국 지나가요 🔥",
            "당신의 감정은 존중받을 자격이 있어요 💪",
            "잠시 숨을 고르고, 스스로를 위로해 주세요 🌌"
        ],
        "songs": [
            ("Imagine Dragons - Believer", "https://youtu.be/7wtfhZwyrcc")
        ]
    },
    "외로움": {
        "messages": [
            "혼자가 아니라는 걸 잊지 마세요 🌌",
            "자신을 사랑하는 순간, 외로움도 사라져요 💖",
            "외로운 마음도 언젠가 따뜻함으로 채워질 거예요 🌷"
        ],
        "songs": [
            ("Ed Sheeran - Perfect", "https://youtu.be/2Vv-BfVoq4g")
        ]
    },
    "설렘": {
        "messages": [
            "가슴 두근거림이 당신을 더 빛나게 하고 있어요 ✨",
            "설레는 순간을 즐기세요 🌸",
            "당신의 설렘이 세상에도 전해지고 있어요 🌈"
        ],
        "songs": [
            ("BTS - Permission to Dance", "https://youtu.be/CuklIb9d3fI")
        ]
    },
    "감사": {
        "messages": [
            "당신이 느끼는 감사가 주변 사람들에게도 전해져요 💕",
            "작은 감사의 마음이 큰 행복으로 돌아올 거예요 🌼",
            "오늘 느낀 감사, 오래도록 간직하세요 🌟"
        ],
        "songs": [
            ("Jason Mraz - I'm Yours", "https://youtu.be/EkHTsc9PU2A")
        ]
    },
    "사랑": {
        "messages": [
            "사랑하는 마음이 당신을 더 빛나게 해요 💖",
            "오늘 느낀 사랑, 당신을 행복하게 할 거예요 🌹",
            "당신의 마음이 전해져 세상도 따뜻해지고 있어요 🌈"
        ],
        "songs": [
            ("Ed Sheeran - Perfect", "https://youtu.be/2Vv-BfVoq4g")
        ]
    }
}

st.title("🌸 감정 힐링 & 노래 추천 🌸")
st.write("지금 느끼는 감정을 입력하면 따뜻한 말과 기분 전환 노래를 추천해드려요 💖")

user_input = st.text_input("💌 오늘의 감정을 적어보세요 (예: 행복, 슬픔, 설렘...)")

if user_input:
    matched = False
    for key in emotion_data:
        if key in user_input:
            data = emotion_data[key]
            st.success(random.choice(data["messages"]))
            song = random.choice(data["songs"])
            st.markdown(f"🎵 **추천 노래:** [{song[0]}]({song[1]})")
            matched = True
            break
    if not matched:
        st.info("특별한 당신을 위한 따뜻한 말 💖: 오늘도 충분히 잘하고 있어요. 💫")

    
