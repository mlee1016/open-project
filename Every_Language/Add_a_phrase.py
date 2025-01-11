import streamlit as st
import pandas as pd

from Every_korean_ph import *
from Every_german_ph import *
from russian_ph2 import *
from All_Japanese_ph import *
from Every_Italian_ph import *
la = st.selectbox("Choose a language",("Select","Korean","Russian","Italian","Japanese","German"),placeholder="select a language")
st.title("Add some phrases")
upload_file = st.file_uploader("Choose a csv file: ",type="csv")

if upload_file is not None:
  df = pd.read_csv(upload_file)
  name_of_Phrases:str = st.text_input("Add a name to list")
  user_phrase = df.columns.tolist()
  if la == 'Japanese':
    user_phrase_1=df[[user_phrase[0],user_phrase[1],user_phrase[2]]].to_numpy().tolist()
  else:
    user_phrase_1 = df[[user_phrase[0],user_phrase[1]]].to_numpy().tolist()
  st.write("Check if phrases is correct then click submit")
  st.write(df)
  if st.button("submit"):
    if la == "Korean":
      user_custom = Korean(name_of_Phrases,user_phrase_1)
      All_korean_lists.append(user_custom)
    elif la == "German":
      
      
      user_custom = Korean(name_of_Phrases,user_phrase_1)
      All_German_lists.append(user_custom)
    elif la == "Italian":
      
      
      user_custom = Korean(name_of_Phrases,user_phrase_1)
      All_Italian_lists.append(user_custom)
    elif la == "Japanese":
      
      user_custom = Korean(name_of_Phrases,user_phrase_1)
      All_Japanese_lists.append(user_custom)
    elif la == "Russian":
      
      user_custom = Korean(name_of_Phrases,user_phrase_1)
      All_russian_lists.append(user_custom)
    else:
      st.write("Choose a language")

    st.success("Success")
