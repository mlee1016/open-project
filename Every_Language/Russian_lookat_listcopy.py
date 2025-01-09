import streamlit as st
import pandas as pd

from russian_ph2 import *



col1, col2, col3, col4 = st.columns(4)


with col1:
  
  st.write(All_russian_lists[0].de_ru_name)
  df_1 = pd.DataFrame(All_russian_lists[0].de_ru_List)
  st.write(df_1)


with col2:
  st.write(All_russian_lists[1].de_ru_name)
  df_1 = pd.DataFrame(All_russian_lists[1].de_ru_List)
  st.write(df_1)

with col3: 
  st.write(All_russian_lists[2].de_ru_name)
  df_1 = pd.DataFrame(All_russian_lists[2].de_ru_List)
  st.write(df_1)

  
with col4: 

  #st.audio("korean_phrases_\korean_present_polite.mp3",format="audio/mp3")
  st.write(All_russian_lists[3].de_ru_name)
  df_1 = pd.DataFrame(All_russian_lists[3].de_ru_List)
  st.write(df_1)


with col1:
  
  st.write(All_russian_lists[4].de_ru_name)
  df_1 = pd.DataFrame(All_russian_lists[4].de_ru_List)
  st.write(df_1)


with col2:
  st.write(All_russian_lists[5].de_ru_name)
  df_1 = pd.DataFrame(All_russian_lists[5].de_ru_List)
  st.write(df_1)

with col3:
  #st.audio("korean_phrases_\korean_past_polite.mp3",format="audio/mp3")
  st.write(All_russian_lists[6].de_ru_name)
  df_1 = pd.DataFrame(All_russian_lists[6].de_ru_List)
  st.write(df_1)




  
#with col4: 
  #st.write(All_korean_lists[7].de_ko_name)
  #df_1 = pd.DataFrame(All_korean_lists[7].de_ko_List)
 # st.write(df_1)



df_2 = pd.DataFrame(All_words_russian)
st.write("All words: ",df_2)