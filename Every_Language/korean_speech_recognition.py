import speech_recognition
from Every_korean_ph import *
import streamlit as st
import pyttsx3
st.header('Testing speaking')
korean_study_ist = []
for i in range(len(All_korean_lists)):
   
  korean_study_ist.append(f'{i+1}: {All_korean_lists[i].de_ko_name}')
                                                

options:str = st.selectbox("Pick a list to study:",(
    korean_study_ist
  ),index=None,placeholder="Select List")


if options != None or options == "":
    
    studying_list = []
#if (int(options[2])%2 != 0): 
    studying_list:list = All_korean_lists[int(str(options[0]))-1].de_ko_List

#os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/path/to/file.json"

    #print('Credendtials from environ: {}'.format(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))
    # Initialize recognizer class (for recognizing the speech)
    #st.audio("100_Korean_Phrases_for_beginners_#02_formal_informal_Self-StudyKorean.wav",format="audio/wav")
    
    st.write(*studying_list[0])
    r = speech_recognition.Recognizer()
    #lang = ""
    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    #st.write("Test your language speaking.")
    #if st.toggle("Korean"):
      #lang = "ko-KR"



    if st.button("Press",help="press then speak"):
      with speech_recognition.Microphone() as source:
          r.adjust_for_ambient_noise(source,duration=0.2)
          st.write("Talk")
          audio_text = r.listen(source)
          st.write("Time over, thanks")
      # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
          
      try:
              # using google speech recognition
            phrases_ = r.recognize_google(audio_text,language="ko-KR")
            st.write(phrases_)
      except:
            st.write("Sorry, I did not get that")


#sns.load_dataset()


#audio_ = AudioSegment.from_mp3(r"C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\Korean.mp3")
#audio_.export("temp.wav", format="wav")
#with sr.AudioFile("temp.wav") as source:
  #audio = r.record(source)

#try:
  #phrase_text = r.recognize_google(audio,language="ko-KR")
  #print(phrase_text)


#except sr.UnknownValueError:
 # print("Doesnt work")

#except sr.RequestError:
 # print("Request Error")

#audio__ = AudioSegment.from_wav("temp.wav")
#audio__.export("korean_y.mp3",format="mp3")'''







