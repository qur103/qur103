import streamlit as st
import streamlit.components.v1 as components
import os

# Streamlit 앱의 메인 함수
def main():
    # Streamlit 페이지 제목 설정
    st.set_page_config(
        page_title="게임 속 비매너 행위 예측 연구",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # HTML 파일의 경로를 설정합니다.
    html_file_path = os.path.join("htmls", "index.html")

    # HTML 파일을 읽어서 변수에 저장합니다.
    try:
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_code = f.read()
            # st.components.v1.html 함수를 사용하여 HTML 코드를 렌더링합니다.
            components.html(html_code, height=1200, scrolling=True)
    except FileNotFoundError:
        st.error(f"HTML 파일을 찾을 수 없습니다. '{html_file_path}' 경로를 확인해 주세요.")

if __name__ == "__main__":
    main()
