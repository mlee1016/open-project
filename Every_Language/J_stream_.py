import streamlit as st
from All_Japanese_ph import *
#from audio_ko import ko_polite_present
import pandas as pd
import random
## ignore just a helper function:





def make_alpha(string:str):
    result = ""
    for char in string:
        if char.isalpha():
            result += char
    return result

   #st.rerun()
korean_study_ist = []
for i in range(len(All_Japanese_lists)):
   
  korean_study_ist.append(f'{i+1}: {All_Japanese_lists[i].de_ko_name}')
                                                

options:str = st.selectbox("Pick a list to study:",(
                                                korean_study_ist
  ),index=None,placeholder="Select List",key="Stream_")


if options != None or options == "":
  studying_list = []
#if (int(options[2])%2 != 0): 
  studying_list:list = All_Japanese_lists[int(str(options[0]))-1].de_ko_List
  
  df1 = pd.DataFrame(studying_list)
  sol = df1.columns.tolist()
  studying_list = df1[[sol[1],sol[2]]].to_numpy().tolist()  
  en_ko = df1[[sol[2],sol[1]]].to_numpy().tolist()
    #st.write(*en_ko)
  #else:
    #studying_list:list = list(All_words_korean[int(str(options[0]))-1]) 

    #df1 = pd.DataFrame(studying_list)
    #st.write(df1)
  #df = pd.DataFrame(list(korean_useful_polite_words))
  #st.write(df)
  #############################################
  #for i in range(len(korean_particle_polite.de_ko_List)):
    #t_c = st.container(border=True,key=i)

    #t_c.audio(ko_polite_present[i],format="mp3/audio")   
    
    #t_c.write(korean_particle_polite.de_ko_List[i][0])
    #t_c.write(korean_particle_polite.de_ko_List[i][1])
    #t_c.write(korean_particle_polite.de_ko_List[i][2])



  on = st.toggle("Japanese -> English (Note : need a Japanese Keyboard)")
  if on:
      
      studying_list = en_ko
      #for i in range (len(list(en_ko[st.session_state.a][1]))):
      shuffle_list = list(en_ko[st.session_state.a][1])
      random.shuffle((shuffle_list))
      #st.write(*shuffle_list)
      
      #st.write(list(en_ko[st.session_state.a][1])[i])
      
      
  on2 = st.toggle("No Audio")
  if on2:
    pass
  on3 = st.toggle("No words")
  if on3:
     pass
  def gen2():
    #for s in range(15):
      yield studying_list[0][0]##############Korean present polite
      yield studying_list[1][0]
      yield studying_list[2][0]
    

  y = gen2()

  def get_n() -> str:
    return next(y)
  input_r = ""

  if 'ls' not in st.session_state:
    st.session_state.ls = []
  if 'a' not in st.session_state:
    st.session_state['a'] = 0
  question = get_n()
  #st.write(korean_present_polite.de_ko_List[0][1])
  
  try:  
    if st.session_state.a+1 <= 15:
      st.write(f"{st.session_state.a+1}","/",str(len(studying_list))) 


    #if not on2:
      #st.audio(All_Audio_korean[0][st.session_state['a']], format="mp3/audio")


    current_Phrases = studying_list[st.session_state.a][0]
    if on3:
      current_Phrases = ""
      
    input_r = st.text_input(f"Type the meaning of this phrase '{current_Phrases}' : ",placeholder="Type in English/Japanese",autocomplete=None)
    if on:
      st.write("Shuffled Phrase:")
      st.write(*shuffle_list)
    str1_norm = make_alpha(input_r)
    str2_norm = make_alpha(str(studying_list[st.session_state.a][1]))
    #str1_norm = unicodedata.normalize('NFC', input_r)
    #str2_norm = unicodedata.normalize('NFC', korean_present_polite.de_ko_List[st.session_state.a][1])

    #st.write("".join(str(ord(e)) for e in str1_norm))
    #st.write("".join(str(ord(h)) for h in str2_norm))  

    if str1_norm.upper() == str2_norm.upper():
      question = get_n()
      st.session_state.a +=1
      st.success("correct")
      st.button("->")
    elif str1_norm == "":
      pass
    else:
      st.error("nope")
      
      st.session_state.ls.append(f"{st.session_state.a}")
      
  except(StopIteration,IndexError):
    #if st.session_state.a == len(studying_list):
      st.write("You completed the list.")
      st.write(st.session_state.ls)
      error = set(st.session_state.ls)
      st.write(error)
      st.write(f"%{(st.session_state.a-error.__len__())/(st.session_state.a-1)*100}")
      
      st.balloons()
      #if st.button("again"):
        #st.cache_data.clear()
        #st.session_state.a = 0
        #st.session_state.ls = []
        #st.rerun()
    #else:
      
        #st.cache_data.clear()
        #st.session_state.a = 0
        #st.session_state.ls = []
        #st.rerun()
    
