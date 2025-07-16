import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

# 텍스트를 입력받아서 해당 텍스트와 일치하는 이미지를 반환
#소프트코딩 - 변화가 많은 데이터를 사용할 때는 변수의 변화에 따라 코드도 함께 바뀌며 동작하는 것을 권장합니다.


ani=st.text_input('좋아하는 애니메이션을 입력해주세요')
if ani:
    for ani in ani_list:
        if ani in ani_list:
            st.image(img_list[ani_list.index(ani)])
        else:
            st.write('애니메이션이 없습니다.')