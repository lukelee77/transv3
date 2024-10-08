##### 기본 정보 불러오기 ####
# Streamlit 패키지 추가
import streamlit as st
# OpenAI 패키기 추가
import openai

##### 기능 구현 함수 #####
def askGpt(prompt,apikey):
    client = openai.OpenAI(api_key = apikey)
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}])
    gptResponse = response.choices[0].message.content
    return gptResponse


##### 메인 함수 #####
def main():
    # st.set_page_config(page_title="요약 프로그램")
    st.title("📃해외파트 번역 프로그램 테스트_Ver2 ")  
    st.header('※주의. 개인용 유료 API key 사용 중')  
    st.markdown('---')      
 
 # 사이드바
    with st.sidebar:
        open_apikey = st.text_input(label='OPENAI API키', placeholder='Enter Your API Key', value='', type='password')
    
    text = st.text_area("번역 할 글을 입력하세요")
    if st.button("번역"):
        prompt = f'''
    - 아래 입력한 다국어로 구성된 제품 불량을 전문적으로 번역하는 역할을 수행해줘.
    - 내가 입력할 데이터는 어떤 국가의 언어를 나타내는지에 대한 국가명, 제품 불량 두가지야.
    - 어떤 국가의 언어인지와 제품 불량 데이터를 구분하기 위해 두 가지 데이터 사이에 --- 이라는 구분자 기호를 사용할 거야.
    - 그러면 국가명을 참조해서 제품 불량을 한국어로 번역해줘.
    - 화면에 보여줄 결과 값은 국가명과 제품 불량을 한국어로 번역한 결과를 한 줄씩 보여줘.
    - 한국어로 번역한 결과를 요약해서 요약 증상도 보여줘.
    - 결과는 생략하지 말고 모두 순서대로 보여주고, 결과물 앞에 번호를 붙여줘
    - 출력 양식은 아래를 참조해줘.
        A: 1. 국가명 --- 제품 불량 --- 한국어 번역결과 --- 요약 증상
            2. 국가명 --- 제품 불량 --- 한국어 번역결과 --- 요약 증상
            3. 국가명 --- 제품 불량 --- 한국어 번역결과 --- 요약 증상
    - 모든 번역값을 출력한 뒤에, 마지막에는 요약 증상에 대해 10개의 유형별로 분류하고 각각의 유형이 몇건인지 표로 요약해줘.
    - 10개의 유형의 마지막은 기타로 표기하고, 요약 증상의 합계는 총 입력수와 동일하게 해줘.
    - text : {text}
    '''
    
        if open_apikey:
            st.info(askGpt(prompt,open_apikey))
        else:
            st.info("API 키를 입력하세요")

if __name__=="__main__":
    main()  


#     ##### 기본 정보 불러오기 ####
# # Streamlit 패키지 추가
# import streamlit as st
# # OpenAI 패키기 추가
# import openai

# ##### 기능 구현 함수 #####
# def askGpt(prompt,apikey):
#     client = openai.OpenAI(api_key = apikey)
#     response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[{"role": "user", "content": prompt}])
#     gptResponse = response.choices[0].message.content
#     return gptResponse

# ##### 메인 함수 #####
# def main():
#     # st.set_page_config(page_title="요약 프로그램")
#     st.header("📃번역 프로그램 테스트")  
#     st.markdown('---')      
 
#  # 사이드바
#     with st.sidebar:
#         open_apikey = st.text_input(label='OPENAI API키', placeholder='Enter Your API Key', value='', type='password')
    
#     text = st.text_area("번역 할 글을 입력하세요")
#     if st.button("번역"):
#         prompt = f'''
#     - 아래 입력한 다국어로 구성된 제품 불량을 전문적으로 번역하는 역할을 수행해줘.
#     - 내가 입력할 데이터는 어떤 국가의 언어를 나타내는지에 대한 국가명, 제품 불량 두가지야.
#     - 어떤 국가의 언어인지와 제품 불량 데이터를 구분하기 위해 두 가지 데이터 사이에 --- 이라는 구분자 기호를 사용할 거야.
#     - 그러면 국가명을 참조해서 제품 불량을 한국어로 번역해줘.
#     - 화면에 보여줄 결과 값은 국가명과 제품 불량을 한국어로 번역한 결과를 한 줄씩 보여줘.
#     - 결과는 순서대로 보여주고, 결과물 앞에 번호를 붙여줘
#     - 출력 양식은 아래를 참조해줘.
#         Q: 1. 국가명 --- 제품 불량
#             2. 국가명 --- 제품 불량
#             3. 국가명 --- 제품 불량
#         A: 1. 국가명 --- 제품 불량 --- 한국어 번역결과
#             2. 국가명 --- 제품 불량 --- 한국어 번역결과
#             3. 국가명 --- 제품 불량 --- 한국어 번역결과
#     - 모든 번역값을 출력한 뒤에, 마지막에는 한국어 번역결과를 10개의 유형별로 분류하고 각각의 유형이 몇건인지 표로 요약해줘.
#     - text : {text}
#     '''
    
#         if open_apikey:
#             st.info(askGpt(prompt,open_apikey))
#         else:
#             st.info("API 키를 입력하세요")

# if __name__=="__main__":
#     main()