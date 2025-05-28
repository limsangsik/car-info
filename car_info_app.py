import streamlit as st
import pandas as pd

# Streamlit 앱의 제목 설정
st.title("차량 정보 조회 앱")

# CSV 파일 로드 (사전에 '차량정보.csv' 파일을 이 스크립트와 동일한 디렉토리에 저장해야 합니다.)
try:
    df = pd.read_csv('차량정보.csv')
except FileNotFoundError:
    st.error("오류: '차량정보.csv' 파일을 찾을 수 없습니다. 파일이 스크립트와 같은 위치에 있는지 확인해주세요.")
    st.stop() # 파일이 없으면 앱 실행 중지

# 사용자 입력 필드
last_4_digits = st.text_input("차량번호 뒷자리 4개 입력", max_chars=4, help="예: 3456")

# 조회 버튼
if st.button("조회"):
    if last_4_digits:
        # 입력된 뒷자리 숫자가 4자리인지 확인
        if len(last_4_digits) != 4 or not last_4_digits.isdigit():
            st.warning("차량번호 뒷자리 4개를 정확히 숫자로 입력해주세요.")
        else:
            # 차량번호 컬럼이 문자열인지 확인하고 .endswith() 사용
            # 혹시 모를 공백이나 문자열이 아닌 데이터 타입을 위해 전처리
            df['차량번호'] = df['차량번호'].astype(str).str.strip()
            results = df[df['차량번호'].str.endswith(last_4_digits)]

            if not results.empty:
                st.subheader("조회 결과:")
                for index, row in results.iterrows():
                    st.write(f"---")
                    st.write(f"**소속:** {row['소속']}")
                    st.write(f"**차주명:** {row['차주명']}")
                    st.write(f"**차량종류:** {row['차량종류']}")
                st.write(f"---")
            else:
                st.warning("해당 차량번호 뒷자리에 해당하는 정보가 없습니다.")
    else:
        st.warning("차량번호 뒷자리 4개를 입력해주세요.")

# 사용법 안내 (선택 사항)
st.markdown("""
<br>
<small>
이 앱은 '차량정보.csv' 파일에 저장된 데이터를 기반으로 차량 정보를 조회합니다.
</small>
""", unsafe_allow_html=True)