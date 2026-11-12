import streamlit as st

# st.title('우리 회사 챗봇')
# st.write('채팅을 입력하세요.')

# st.markdown("안녕하세요 *부트캠프* 여러분!")

# import streamlit as st

# name = st.text_input("이름을 입력하세요")
# age = st.slider("나이", 0, 100, 25)

# if st.button("확인"):
#     st.write(f"{name}님은 {age}살입니다.")


page_1 = st.Page('page_1.py',title='1page')
page_2 = st.Page('page_2.py')
page_3 = st.Page('page_3.py')

pages = st.navigation([page_1, page_2, page_3])
pages.run()