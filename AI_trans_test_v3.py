##### 기본 정보 불러오기 ####
# Streamlit 패키지 추가
import streamlit as st
# OpenAI 패키기 추가
import openai

##### 기능 구현 함수 #####
def askGpt(prompt,apikey):
    # API 키를 안전하게 관리하는 방식으로 설정 (여기서는 Streamlit secrets 사용)
    apikey = st.secrets["openai"]["apikey"]  # 환경변수나 Streamlit secrets에서 가져오기
    openai.api_key = apikey

    client = openai.OpenAI(api_key = apikey)

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}])
    gptResponse = response.choices[0].message.content
    return gptResponse    


##### 메인 함수 #####
def main():
    st.set_page_config(page_title="Translator GPT", page_icon="📖", layout="wide")
    st.title('''Luke's AI 번역 프로그램 테스트_Ver3😏''')
    st.subheader('※ 배포금지. 개인용 유료 API key 사용 (해외시장 전용)')    
    st.text('''Instruction - 아래 번역칸에 "No.국가명 --- 제품불량" 형태로 입력(최대 500줄이하)''')    
    st.text('''출력 형태는 "No. 국가명 --- 제품 불량 --- 한국어 번역결과 --- 요약 증상" ''')    
    st.markdown('---')
  
    text = st.text_area("번역 할 글을 입력하세요")
    if st.button("번역"):
        prompt = f'''
   *** instructions ***
    - 아래 입력한 다국어로 구성된 제품 불량을 전문적으로 번역하는 역할을 수행해줘.
    - 내가 입력할 데이터는 어떤 국가의 언어를 나타내는지에 대한 국가명, 제품 불량 두가지야.
    - 어떤 국가의 언어인지와 제품 불량 데이터를 구분하기 위해 두 가지 데이터 사이에 --- 이라는 구분자 기호를 사용할 거야.
    - 그러면 국가명을 참조해서 제품 불량을 한국어로 번역해줘.
    - 화면에 보여줄 결과 값은 국가명과 제품 불량을 한국어로 번역한 결과를 반드시 한 줄씩 보여줘.
    - 결과는 반드시 생략하지 말고 최대 500줄을 빠짐없이 모두 한 줄씩 순서대로 보여주고, 결과물 앞에 번호를 붙여줘.
    - 한국어로 번역한 결과를 요약해서 간략한 요약 증상도 보여줘.

    - 출력 양식은 아래를 참조해줘.
        1. 국가명 --- 제품 불량 --- 한국어 번역결과 --- 간략한 요약 증상
        2. 국가명 --- 제품 불량 --- 한국어 번역결과 --- 간략한 요약 증상
        3. 국가명 --- 제품 불량 --- 한국어 번역결과 --- 간략한 요약 증상
    
    - 모든 번역값을 출력한 뒤에, 마지막에는 간략한 요약 증상에 대해 최대 20개의 유형별로 분류하고 각각의 유형이 몇건인지 표로 요약해줘.
    - 20개의 유형의 마지막은 기타로 표기하고, 요약 증상의 합계는 총 입력수와 동일하게 해줘.
    - text : {text}
    '''
        apikey = st.secrets["openai"]["apikey"]  # 환경변수나 Streamlit secrets에서 가져오기
        st.info(askGpt(prompt, apikey))  # 수정된 부분: api_key → apikey        

        
if __name__=="__main__":
    main()  
