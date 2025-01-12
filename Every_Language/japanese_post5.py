import streamlit as st
import random


from All_Japanese_ph import *
#from audio_ko import ko_polite_present
import pandas as pd
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
#if 'd' not in st.session_state:
  #st.session_state['d'] = 0
#def clear_cache():
   #st.cache_data.clear()
   #st.rerun()


   #st.rerun()
korean_study_ist = []
for i in range(len(All_Japanese_lists)):
   
  korean_study_ist.append(f'{i+1}: {All_Japanese_lists[i].de_ko_name}')
                                                

if 'e' not in st.session_state:
  st.session_state['e'] = 0

options:str = st.selectbox("Pick a list to study:",(korean_study_ist),index=None,placeholder="Select List")
studying_list = []
studying_list4 = []
if options != None or options == "":
#st.cache_data.clear()
#if int(options[2])%2 != 0: 

  studying_list:list = All_Japanese_lists[int(str(options[0]))-1].de_ko_List
  

  # 0 = kanji : 1 = hiragana/katagana : 2 = english 
  df1 = pd.DataFrame(studying_list)
  sol = df1.columns.tolist()
        
  studying_list = df1[[sol[0],sol[2],sol[1]]].to_numpy().tolist()

  en_ko = df1[[sol[2],sol[0],sol[1]]].to_numpy().tolist()

  
  studying_list4 = df1[[sol[1],sol[2],sol[0]]].to_numpy().tolist()

  en_ko2 = df1[[sol[2],sol[1],sol[0]]].to_numpy().tolist()

    
    #st.rerun()

    


    #if 'no' not in st.session_state:
      #st.session_state.no = False
    #if 'rando_list' not in st.session_state:
      #st.session_state.rando_list = [0,1,2,3]
    #if 'rand_list' not in st.session_state:
      #st.session_state.rand_list = [0,1,2,3]


    #df1 = pd.DataFrame(studying_list)
    #st.write(df1)

    

#else:
  #studying_list:list = list(All_words_korean[int(str(options[0]))-1]) 
  
  
    #st.rerun()

    


  


    
  if 'no' not in st.session_state:
    st.session_state.no = False
  if 'rando_list' not in st.session_state:
    st.session_state.rando_list = [0,1,2,3]
  if 'rand_list' not in st.session_state:
    st.session_state.rand_list = [0,1,2,3]


  on = st.toggle("Japanese -> English")
  if on:
      #st.write("Feature activated!")
      studying_list = en_ko
      #for i in range (len(list(en_ko[st.session_state.a][1]))):
      shuffle_list = list(en_ko[st.session_state.e][1])
      random.shuffle((shuffle_list))
      #st.write(*shuffle_list)
    #df1 = pd.DataFrame(studying_list)
    #st.write(df1)
  h_k = st.toggle("hiragana/katakana")
  if h_k: 
    studying_list = studying_list4
    if on:
      studying_list = en_ko2
     
    #if 'no' not in st.session_state:
      #st.session_state.no = False
    #if 'rando_list' not in st.session_state:
      #st.session_state.rando_list = [0,1,2,3]
    #if 'rand_list' not in st.session_state:
      #st.session_state.rand_list = [0,1,2,3]


  #if 'd' not in st.session_state:
      #st.session_state['d'] = 0

  if options != None:
    @st.cache_data
    def rand_List(n_phrases: int):
      
      st.session_state.rand_list = [None]*len(studying_list)
      for i in range(len(studying_list)):
          st.session_state.rand_list[i] = i
        #print(*rand_list)
      random.shuffle(st.session_state.rand_list)
        #print(*rand_list)
      st.session_state.rando_list = [st.session_state.rand_list[0],st.session_state.rand_list[1],st.session_state.rand_list[2]]
      st.session_state.rando_list.append(st.session_state.e)
      #print(*st.session_state.rando_list)
      random.shuffle(st.session_state.rando_list)
      return st.session_state.rando_list
      #print(*st.session_state.rando_list)
      


    def nextQuestion():
      st.session_state['e'] +=1

    #a1 = studying_list[st.session_state.rando_list[0]][1]
    #a2 = studying_list[st.session_state.rando_list[1]][1]
    #a3 = studying_list[st.session_state.rando_list[2]][1]
      #a4 = studying_list[st.session_state.rando_list[3]][1]
  try:
      if st.session_state.e < len(studying_list):
        st.write("Question:",str(st.session_state.e+1),"/",str(len(studying_list)))
      #if korean_present_polite.getDefault_Name() == "Korean Present Polite Speech:":
      
      #if on == False:
        #st.audio(All_Audio_korean[0][st.session_state['e']], format="wav/audio")
      question = st.radio(f"What does this mean: {studying_list[st.session_state['e']][0]}",[" ",studying_list[rand_List(st.session_state.e)[0]][1],studying_list[rand_List(st.session_state.e)[1]][1],studying_list[rand_List(st.session_state.e)[2]][1],studying_list[rand_List(st.session_state.e)[3]][1]])
      if studying_list[st.session_state.e][1] == question:
          st.success("Correct")

      elif " " == question:
          pass
      else:
          #st.write("Nope")


        st.error("Nope")
        
      st.button("->",on_click=nextQuestion)
  except(IndexError):
    
    
    st.write("You completed the list.")
    #st.write(st.session_state.ls)
    #error = set(st.session_state.ls)
    #st.write(error)
    #st.write(f"%{(st.session_state.a-error.__len__())/(st.session_state.a-1)*100}")
        
    #st.balloons()
    if st.button("study again"):
      st.cache_data.clear()
      st.session_state['e'] = 0
      studying_list = []
      st.rerun()
