import os
from openai import OpenAI
import time

#웹사이트에서 글씨쓰는 코드
import streamlit as st
# 코드스니펫 - 제목
st.title('영선이가 처음 만든거')

# 코드스니펫 - 입력
keyword = st.text_input("키워드를 입력하세요.")

# 코드스니펫 - 버튼
if st.button('만들기'):
  st.write('나만의 제품 만들기')
  #with 밑으로는 들여쓰기 하기(with 보다 안쪽으로 하기)

  with st.spinner('Wait for it...'):
    #time.sleep(5)  #5초 동안 돌악가게 만드는 코드
    #st.success('Done!')

    client = OpenAI(api_key=st.secrets["API_KEY"])

    chat_completion = client.chat.completions.create(
        messages=[{
            "role":
            "user",
            "content":
            keyword + '라는 주제로 새로운 제품을 홍보할 수 있는 카피를 150자 이내로 작성해줘'
        }],
        model="gpt-4o",
    )

    chat_result = chat_completion.choices[0].message.content

    # 코드스니펫 - 글쓰기
    st.write(chat_result)

    # 이미지 만들기

    client = OpenAI(api_key=st.secrets["API_KEY"])

    response = client.images.generate(
        model="dall-e-3",
        prompt=keyword,  #위에 글에 대한 이미지라서 chat result로 작성 or keyword,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url

    st.image(image_url)
