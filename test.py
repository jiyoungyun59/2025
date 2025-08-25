import streamlit as st
from collections import Counter
import requests

# ----------------------------
# 단어 정보 가져오기 (Dictionary API 사용)
# ----------------------------
def get_word_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()[0]
        meaning = data["meanings"][0]["definitions"][0]["definition"]
        example = data["meanings"][0]["definitions"][0].get("example", "예문 없음")
        phonetic = data.get("phonetic", "")
        return meaning, example, phonetic
    else:
        return "정의 없음", "예문 없음", ""

# ----------------------------
# Streamlit UI
# ----------------------------
st.title("📖 영어 단어 학습 분석 앱")
st.write("영어 단어를 입력하면 뜻, 예문, 발음과 함께 간단한 빈도 분석을 제공합니다!")

# 단어 입력
word = st.text_input("단어를 입력하세요:", "")

if word:
    # 단어 정보 출력
    meaning, example, phonetic = get_word_definition(word)
    st.subheader(f"🔎 단어 정보: {word}")
    st.write(f"**발음**: {phonetic}")
    st.write(f"**뜻**: {meaning}")
    st.write(f"**예문**: {example}")

    # 샘플 텍스트 데이터 (나중에 실제 기사/텍스트로 확장 가능)
    sample_text = """
    Democracy is the government of the people, by the people, for the people.
    Freedom and rights are essential in a democracy.
    A strong government protects the rights of its citizens.
    """
    words = sample_text.lower().split()
    counter = Counter(words)

    # 빈도 그래프 (Streamlit 기본 차트 사용)
    st.subheader("📊 단어 빈도 분석")
    st.bar_chart(dict(counter))

    # 학습 리스트 저장
    if "learned_words" not in st.session_state:
        st.session_state["learned_words"] = []

    if st.button("👉 단어 학습 목록에 추가"):
        st.session_state["learned_words"].append(word)
        st.success(f"'{word}' 단어가 학습 목록에 추가되었습니다!")

# 학습 목록 보기
if "learned_words" in st.session_state:
    st.subheader("📚 나의 학습 목록")
    st.write(st.session_state["learned_words"])


