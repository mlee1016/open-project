import streamlit as st
import pandas as pd

from russian_ph2 import *

from konlpy.tag import Okt









st.markdown(
        """
    <style>
        div[role=radiogroup] label:first-of-type {
            visibility: hidden;
            height: 0px;
        }
        

        audio {
            filter: sepia(50%) saturate(80%) contrast(99%) invert(72%);
            width: 15px;
            height: 22px;
    
        }
    </style>

    """,
        unsafe_allow_html=True,
    )

   #st.rerun()
korean_study_ist = []
for i in range(len(All_russian_lists)):
   
  korean_study_ist.append(f'{i+1}: {All_russian_lists[i].de_ru_name}')
                                                
                                                


options:str = st.selectbox("Pick a list to study:",(
      korean_study_ist
  ),index=None,placeholder="Select List")

studying_list = []
if options != None or options == "":
  
  
  
  
  
#if (int(options[2])%2 != 0): 
  studying_list:list = All_russian_lists[int(str(options[0]))-1].de_ru_List

  df1 = pd.DataFrame(studying_list)
  sol = df1.columns.tolist()
  en_ko = df1[[sol[1],sol[0]]].to_numpy().tolist()
#st.write(*en_ko)
  #else:
    #studying_list:list = list(All_words_russian[int(str(options[0]))-1]) 

  #df1 = pd.DataFrame(studying_list)
  #st.write(df1)
# Initialize a variable in session state if it doesn't exist
  
  try:
    if 'num' not in st.session_state:
        st.session_state['num'] = 0

    st.title("Reviewing Phrases")
    st.divider()

    #with open(r'C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\Russian-phrases.csv', encoding="utf-8") as f:
        #reader = csv.reader(f)
        #your_list = list(reader)

    s = st.container(border=True)
    s.write(str(st.session_state['num']+1)+"/"+str(len(studying_list)))
    s.subheader(studying_list[st.session_state['num']][0])
    
    h = studying_list[st.session_state['num']][0]

    #okt = Okt()
    #pos_tags = okt.pos(h)
    #for p in range(len(pos_tags)):
      #s.write(f"{pos_tags[p][0]} =  {pos_tags[p][1]}")

    #s.audio(All_Audio_korean[0][st.session_state["num"]],format="audio/mp3",autoplay=True)
    s.subheader(studying_list[st.session_state['num']][1])

    def prePhrase():
      
      if st.session_state['num'] <= 0:
        st.cache_data.clear()
        st.session_state['num'] = len(studying_list)-1

      else:  
        st.session_state['num'] -= 1
    def nextPhrase():
      

      if st.session_state['num'] >= len(studying_list)-1:
        st.cache_data.clear()
        st.session_state['num'] = 0
      else:   
        st.session_state['num'] += 1
    col1,col2 = st.columns([12,1])
    with col1:
      st.button("<-", on_click=prePhrase)
    with col2:
      st.button("->",on_click=nextPhrase)
  except(StopIteration,IndexError):

    
    st.cache_data.clear()
    st.session_state["num"] = 0
    st.rerun()

        





    


