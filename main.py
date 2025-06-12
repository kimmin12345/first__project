import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(page_title="가위✌️ 바위✊ 보✋ 게임", page_icon="🎮", layout="centered")

# 제목
st.markdown("# 🎮 가위 ✌️ 바위 ✊ 보 ✋ 게임!")
st.markdown("## 🤖 컴퓨터와 한 판 붙어보자! 💥")

# 이모지 맵
emoji_map = {
    "가위": "✌️",
    "바위": "✊",
    "보": "✋"
}

# 선택지
choices = ["가위", "바위", "보"]

# 사용자 선택
st.markdown("### 당신의 선택은? 😎")
user_choice = st.radio("👇 아래에서 선택하세요!", choices, horizontal=True)

# 버튼
if st.button("👊 대결 시작!"):
    # 컴퓨터 선택
    computer_choice = random.choice(choices)

    # 결과 출력
    st.markdown(f"### 당신의 선택: **{user_choice} {emoji_map[user_choice]}**")
    st.markdown(f"### 컴퓨터의 선택: **{computer_choice} {emoji_map[computer_choice]}**")

    # 승패 결정
    if user_choice == computer_choice:
        result = "😐 비겼어요!"
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        result = "🎉 당신이 이겼어요!"
    else:
        result = "💀 컴퓨터가 이겼어요..."

    # 결과 표시
    st.markdown(f"## 🏁 결과: **{result}**")

    # 이모지로 마무리
    if "이겼어요" in result:
        st.balloons()
    elif "비겼어요" in result:
        st.markdown("😅 다음에 다시 도전해요!")
    else:
        st.markdown("😭 분하다... 다시 도전!")

# 하단 꾸미기
st.markdown("---")
st.markdown("🧠 Tip: 전략적으로 플레이해보세요! 컴퓨터도 패턴이 있을지도...? 😉")
st.markdown("Made with ❤️ by ChatGPT + Streamlit")
