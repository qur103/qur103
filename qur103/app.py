# Streamlit과 pathlib 라이브러리를 임포트합니다.
# pathlib는 파일 경로를 다루는 데 유용합니다.
# codecs는 파일 인코딩 문제를 해결하기 위해 사용합니다.
import streamlit as st
import pathlib
import codecs

# 페이지의 제목을 설정합니다.
st.set_page_config(page_title="HTML 렌더링", layout="wide")
st.title("HTML 파일 불러오기")

# HTML 파일이 위치한 경로를 설정합니다.
# 사용자의 요청에 따라 'htmls' 폴더 내의 'index.html'을 가리킵니다.
html_file_path = pathlib.Path("./htmls/index2.html")

try:
    # 지정된 경로에 파일이 있는지 확인합니다.
    if html_file_path.exists():
        # HTML 파일을 'utf-8' 인코딩으로 열어서 내용을 읽습니다.
        with codecs.open(html_file_path, 'r', 'utf-8') as f:
            html_content = f.read()

        # Streamlit의 components 모듈을 사용하여 HTML을 렌더링합니다.
        # height 매개변수를 사용하여 렌더링된 컴포넌트의 높이를 조정할 수 있습니다.
        st.components.v1.html(html_content, height=800, scrolling=True)

        st.success("HTML 파일을 성공적으로 불러왔습니다.")
    else:
        # 파일이 없을 경우 경고 메시지를 표시합니다.
        st.warning(f"경고: 지정된 경로에 HTML 파일이 없습니다. 경로를 확인해주세요: {html_file_path}")

except Exception as e:
    # 파일을 불러오는 과정에서 오류가 발생하면 오류 메시지를 출력합니다.
    st.error(f"오류가 발생했습니다: {e}")

# 추가적으로 앱에 대한 설명이나 안내를 추가할 수 있습니다.
st.markdown(
    """
    ---
    ### 사용법
    1. 이 코드를 `app.py`로 저장합니다.
    2. `app.py`와 같은 위치에 `htmls` 폴더를 생성합니다.
    3. `htmls` 폴더 안에 `index.html` 파일을 저장합니다.
    4. 터미널에서 `streamlit run app.py` 명령어를 실행하여 앱을 시작합니다.
    """
)
