import csv
import copy
from audio_ko import ko_polite_present, ko_polite_useful 
default_Ko_Ph = [[] for i in range(7)]
with open('Every_Language/korean_present_polite.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_Ko_Ph[0] = list(reader)
with open('Every_Language/korean_past_polite.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_Ko_Ph[1] = list(reader)


with open('Every_Language/korean_future_polite.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_Ko_Ph[2] = list(reader)

with open('Every_Language/korean_past_polite2.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_Ko_Ph[3] = list(reader)
with open('Every_Language/korean_future_polite2.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_Ko_Ph[4] = list(reader)


with open('Every_Language/korean_useful_phrases.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_Ko_Ph[5] = list(reader)


with open('Every_Language/korean_grammar_particle.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_Ko_Ph[6] = list(reader)

#print(default_Ko_Ph)


#list_15_ko = [default_Ko_Ph[y:y+15] for y in range(0,len(default_Ko_Ph),15)]
#print(list_15_ko[0])


class Korean():
    # cu = custom / ko = korean/ de = default 
    de_ko_List = []
    de_ko_name = ""
    cu_ko_List = []
    cu_ko_name = ""
    se_ = 0
    def __init__(self,k_name:str,ko_list):
        self.de_ko_List = ko_list
        self.de_ko_name = k_name
        Korean.se_ +=1
    def customRuList(self, k_r_name, k_ru_List):
        self.ko_ru_List = k_ru_List
        self.ko_ru_name = k_r_name
    def getCustom_Name(self) -> str:
        return self.cu_ko_name
    def getDefault_Name(self) -> str:
        return self.de_ko_name
    
    def getList(self,name:str):
        if self.de_ko_name == name:
            return self.de_ko_List
        return []
    def return_ie():
        return Korean.se_
korean_present_polite = Korean("Korean Present Polite Speech: ",copy.deepcopy(default_Ko_Ph[0]))
#print(len(korean_present_polite.de_ko_List))

korean_present_polite_words = set()
str_kp = []
col_ = []
for s in range(len(korean_present_polite.de_ko_List)):
    col_.append(korean_present_polite.de_ko_List[s][0])


for i in range(len(col_)):
  str_kp.extend(col_[i].split())
for d in range(len(str_kp)):
    korean_present_polite_words.add(str_kp[d])

print(1, len(korean_present_polite_words))

korean_past_polite = Korean("Korean Past Polite Speech: ",copy.deepcopy(default_Ko_Ph[1]))
#print(len(korean_past_polite.de_ko_List))

korean_past_polite_words = set()
str_kp2 = []
col_o2 = []

for s in range(len(korean_past_polite.de_ko_List)):
    col_o2.append(korean_past_polite.de_ko_List[s][0])


for i in range(len(col_o2)):
  str_kp2.extend(col_o2[i].split())
for d in range(len(str_kp2)):
    korean_past_polite_words.add(str_kp2[d])
#print(len(str_kp2))
print(2, len(list(korean_past_polite_words)))


korean_future_polite = Korean("Korean Future Polite Speech: ",copy.deepcopy(default_Ko_Ph[2]))
#print(len(korean_future_polite.de_ko_List))
#print(korean_future_polite.de_ko_List[1][0])

korean_future_polite_words = set()
str_kp3 = []
col_o3 = []


for s in range(len(korean_future_polite.de_ko_List)):
    col_o3.append(korean_future_polite.de_ko_List[s][0])



for i in range(len(col_o3)):
  str_kp3.extend(col_o3[i].split())
for d in range(len(str_kp3)):
    korean_future_polite_words.add(str_kp3[d])
#print(len(str_kp3))
print(3, len(list(korean_future_polite_words)))

korean_past_polite2 = Korean("Korean Past Polite Speech 2: ",copy.deepcopy(default_Ko_Ph[3]))
#print(len(korean_past_polite2.de_ko_List))

korean_past_polite2_words = set()
str_kp4 = []
col_o4 = []


for s in range(len(korean_past_polite2.de_ko_List)):
    col_o4.append(korean_past_polite2.de_ko_List[s][0])


for i in range(len(col_o4)):
  str_kp4.extend(col_o4[i].split())
for d in range(len(str_kp4)):
    korean_past_polite2_words.add(str_kp4[d])

#print(len(str_kp4))
print(4, len(list(korean_past_polite2_words)))

korean_future_polite2 = Korean("Korean Future Polite Speech2: ",copy.deepcopy(default_Ko_Ph[4]))
#print(len(korean_future_polite2.de_ko_List))

korean_future_polite2_words = set()
str_kp5 = []
col_o5 = []


for s in range(len(korean_future_polite2.de_ko_List)):
    col_o5.append(korean_future_polite2.de_ko_List[s][0])


for i in range(len(col_o5)):
  str_kp5.extend(col_o5[i].split())
for d in range(len(str_kp5)):
    korean_future_polite2_words.add(str_kp5[d])
#print(len(str_kp5))
print(5, len(list(korean_future_polite2_words)))

korean_useful_polite = Korean("Korean Useful Phrases: ",copy.deepcopy(default_Ko_Ph[5]))
#print(len(korean_useful_polite.de_ko_List))


korean_useful_polite_words = set()
str_kp6 = []
col_o6 = []


for s in range(len(korean_useful_polite.de_ko_List)):
    col_o6.append(korean_useful_polite.de_ko_List[s][0])


for i in range(len(col_o6)):
  str_kp6.extend(col_o6[i].split())
for d in range(len(str_kp6)):
    korean_useful_polite_words.add(str_kp6[d])
#print(len(str_kp6))
print(6, len(list(korean_useful_polite_words)))

korean_particle_polite = Korean("Korean Particle Phrases: ",copy.deepcopy(default_Ko_Ph[6]))
#print(len(korean_particle_polite.de_ko_List))


korean_particle_polite_words = set()
str_kp7 = []
col_o7 = []




for t in range(len(korean_particle_polite.de_ko_List)):
    col_o7.append(korean_particle_polite.de_ko_List[t][0])


for i in range(len(col_o7)):
  str_kp7.extend(col_o7[i].split())
for d in range(len(str_kp7)):
    korean_particle_polite_words.add(str_kp7[d])
#print(len(str_kp7))
print(7, len(list(korean_particle_polite_words)))



    q_a_response = ['''

    **1.**  
    **Q:** 이름이 뭐예요? *What is your name?*  
    (*Ireumi mwoyeyo?*) ''','''
    **A:** 제 이름은 민준이에요. *My name is Min-jun.*  
    (*Je ireumeun Minjun-ieyo.*)  ''',
    '''
    **2.**  
    **Q:** 어디에서 왔어요? *Where are you from?*  
    (*Eodieseo wasseoyo?*)  ''','''
    **A:** 저는 미국에서 왔어요. *I’m from the U.S.*  
    (*Jeoneun Migug-eseo wasseoyo.*)  ''',
    '''
    **3.**  
    **Q:** 몇 살이에요? *How old are you?*  
    (*Myeot sal-ieyo?*)  ''','''
    **A:** 저는 스물다섯 살이에요. *I’m 25 years old.*  
    (*Jeoneun seumul-daseot sal-ieyo.*)  ''',
    '''
    **4.**  
    **Q:** 오늘 날씨가 어때요? *How’s the weather today?*  
    (*Oneul nalssiga eottaeyo?*)  ''','''
    **A:** 날씨가 정말 좋아요. *The weather is really nice.*  
    (*Nalssiga jeongmal joayo.*)  ''',
    '''
    **5.**  
    **Q:** 무슨 일을 하세요? *What do you do for a living?*  
    (*Museun ireul haseyo?*)  ''','''
    **A:** 저는 학생이에요. *I’m a student.*  
    (*Jeoneun haksaeng-ieyo.*)  ''',
    '''
    **6.**  
    **Q:** 지금 몇 시예요? *What time is it now?*  
    (*Jigeum myeot si-yeyo?*)  ''','''
    **A:** 지금 두 시예요. *It’s 2 o’clock now.*  
    (*Jigeum du si-yeyo.*)  ''',
    '''
    **7.**  
    **Q:** 이거 얼마예요? *How much is this?*  
    (*Igeo eolmayeyo?*)  ''','''
    **A:** 이거 만 원이에요. *This is 10,000 won.*  
    (*Igeo man won-ieyo.*)  ''',
    '''
    **8.**  
    **Q:** 화장실 어디예요? *Where is the restroom?*  
    (*Hwajangsil eodieyo?*)  ''','''
    **A:** 저쪽이에요. *It’s over there.*  
    (*Jeojjok-ieyo.*)  ''',
    '''
    **9.**  
    **Q:** 좋아하는 음식이 뭐예요? *What is your favorite food?*  
    (*Joahaneun eumsigi mwoyeyo?*)  ''','''
    **A:** 저는 김치를 좋아해요. *I like kimchi.*  
    (*Jeoneun gimchi-reul joahaeyo.*)  ''',
    '''
    **10.**  
    **Q:** 한국어를 잘해요? *Do you speak Korean well?*  
    (*Hangugoreul jalhaeyo?*)  ''','''
    **A:** 아니요, 아직 잘 못해요. *No, I can’t speak it well yet.*  
    (*Aniyo, ajik jal motaeyo.*)  ''',
    '''
    **11.**  
    **Q:** 취미가 뭐예요? *What is your hobby?*  
    (*Chwimiga mwoyeyo?*)  
    ''','''
    **A:** 제 취미는 음악 듣기예요. *My hobby is listening to music.*  
    (*Je chwimineun eumak deutgi-yeyo.*)  ''',
    '''
    **12.**  
    **Q:** 이 길로 가면 돼요? *Is it okay to go this way?*  
    (*I gillo gamyeon dwaeyo?*)  ''','''
    **A:** 네, 맞아요. *Yes, that’s correct.*  
    (*Ne, majayo.*)  ''',
    '''
    **13.**  
    **Q:** 사진 좀 찍어 주시겠어요? *Could you take a picture for me?*  
    (*Sajin jom jjigeo jusigesseoyo?*)  ''','''
    **A:** 네, 물론이죠. *Yes, of course.*  
    (*Ne, mullonijyo.*)  ''',
    '''
    **14.**  
    **Q:** 오늘 뭐 할 거예요? *What are you going to do today?*  
    (*Oneul mwo hal geoyeyo?*)  ''','''
    **A:** 저는 친구를 만날 거예요. *I’m going to meet a friend.*  
    '(*Jeoneun chingureul mannal geoyeyo.*)  ''',
    '''
    **15.**  
    **Q:** 다시 말해 줄 수 있어요? *Can you say that again?*  
    (*Dasi malhae jul su isseoyo?*)  ''','''
    **A:** 네, 다시 말씀드릴게요. *Yes, I’ll say it again.*  
    (*Ne, dasi malsseumdeurilgeyo.*) ''']

#korean_q_a = Korean('Q and A',q_a_response)
All_korean_lists = [korean_useful_polite,korean_particle_polite,korean_past_polite2,korean_present_polite,
korean_future_polite,korean_future_polite2,korean_past_polite]

All_words_korean = [korean_useful_polite_words,korean_particle_polite_words,korean_past_polite2_words,
korean_present_polite_words,korean_future_polite_words,korean_future_polite2_words,korean_past_polite_words]

All_Audio_korean = [None]*len(All_korean_lists)
All_Audio_korean[0] = ko_polite_useful
All_Audio_korean[3] = ko_polite_present

All_words_ = list(korean_useful_polite_words)+list(korean_particle_polite_words)+list(korean_past_polite2_words)+list(korean_present_polite_words)+list(korean_future_polite_words)+list(korean_future_polite2_words)+list(korean_past_polite_words)



from gtts import *

#for i in range(len(korean_useful_polite.de_ko_List)):

    #tts = gTTS(korean_useful_polite.de_ko_List[i][0], lang='ko')
    #tts.save(fr"C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\korean_phrases_\korean_useful_{i}.mp3")
