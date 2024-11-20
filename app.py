# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('/content/Medicaldataset 최종ㄱㅗㅗㅗ.xlsx') 
# 2. 모델 설명
.title('심장마비 여부 분류 모델')
col1, col2,col3 = st.columns(  )      # 몇 개의 컬럼으로 나눌까?
with col1:
      st.subheader('모델 설명 ')
      st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
      st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
      st.write(' - 훈련    데이터 : 923건')
      st.write(' - 테스트 데이터 : 396건')
      st.write(' - 모델 정확도 : 0.79') 

# 3. 데이터시각화
with col2:
      st.subheader('데이터시각화1')
      st.image('/content/시각화1.png' )   # 이미지 불러오기
with col3:
      st.subheader('데이터시각화2')
      st.image('/content/시각화2.png')  
with col4:
      st.subheader('데이터시각화3')
      st.image('/content/시각화3.png')
with col5:
      st.subheader('데이터시각화4')
      st.image('/content/시각화4.png')
with col6:
      st.subheader('데이터시각화5')
      st.image('/content/시각화5.png')

# 4. 모델 활용
.subheader('모델 활용')
st.write('**** 나이,심박수,CK-MB,트로포닌을 입력해주세요... 인공지능이 당신의 심장마비 여부를 알려드립니다!')

a = st.number_input(' _________ ', value=0)
b = st.number_input(' _________ ', value=0)
c = st.number_input(' _________ ', value=0)
d = st.number_input(' _________ ', value=0)

if st.button('여부 확인'):              # 사용자가 '합불분류' 버튼을 누르면
        input_data = [[ a,b,c,d ]]          # 사용자가 입력한 a,b,c 를 input_data에 저장하고
        p = model._______(input_data)      # model이 분류한 값을 p에 저장한다
        if p[0] == 1 :
              st.success('인공지능 분류 결과는 양성입니다')
        else:
              st.success('인공지능 분류 결과를 음성입니다')
