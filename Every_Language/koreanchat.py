import streamlit as st
try: 
    prompt = ""
    some_list = []
    name_of_list = ["Introduction","Easy Phrases","Q/A"]
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

    easy_Phrases = []
    for s in range(len(easy_phrases)):

        easy_Phrases.append(easy_phrases[s] +" : "+ Easy_phrases[s])
    response_ = ['''**민준:** 안녕하세요! 저는 민준이에요. 이름이 뭐예요?
            (*Annyeonghaseyo! Jeoneun Minjun-ieyo. Ireumi mwoyeyo?*)
            *Hello! I’m Min-jun. What’s your name?*''',

            '''**지훈:** 안녕하세요, 저는 지훈이에요. 만나서 반가워요.
            (*Annyeonghaseyo, jeoneun Jihoon-ieyo. Mannaseo bangawoyo.*)
            *Hello, I’m Ji-hoon. Nice to meet you.*  ''',

            '''**민준:** 저도 만나서 반가워요, 지훈 씨.  
            (*Jeodo mannaseo bangawoyo, Jihoon-ssi.*)  
            *Nice to meet you too, Ji-hoon.*  ''',

            '''**지훈:** 민준 씨는 어디에서 오셨어요?  
            (*Minjun-ssi-neun eodieseo osyeosseoyo?*)  
            *Min-jun, where are you from?*  ''',

            '''**민준:** 저는 서울에서 왔어요. 지훈 씨는요?  
            (*Jeoneun Seoureseo wasseoyo. Jihoon-ssi-neunyo?*)  
            *I’m from Seoul. How about you?*  ''',

        ''' **지훈:** 저는 부산에서 왔어요. 서울은 어때요?  
            (*Jeoneun Busaneseo wasseoyo. Seoureun eottaeyo?*)  
            *I’m from Busan. How is Seoul?*  ''',

        ''' **민준:** 서울은 정말 바쁘고 재미있는 곳이에요. 부산은요?  
            (*Seoureun jeongmal bappeugo jaemiinneun gos-ieyo. Busan-eunyo?*)  
            *Seoul is a very busy and fun place. How about Busan?*''',

            '''**지훈:** 부산은 바다가 예쁘고 음식이 맛있어요.  
            (*Busaneun badaga yeppeugo eumsigi masisseoyo.*)  
            *Busan has beautiful beaches and delicious food.*  ''',

        ''' **민준:** 아, 정말요? 나중에 부산에 꼭 가 보고 싶어요.  
            (*A, jeongmalyo? Najunge Busan-e kkok ga bogo sipeoyo.*)  
            *Oh, really? I’d love to visit Busan someday.* ''' ,

        ''' **지훈:** 네, 오시면 제가 맛집을 소개할게요.  
            (*Ne, osimyeon jega matjibeul sogaehalkkeyo.*)  
            *Yes, if you come, I’ll introduce you to some great restaurants.*  ''',

        ''' **민준:** 감사합니다! 지훈 씨는 뭐 하는 일을 하세요?  
            (*Gamsahamnida! Jihoon-ssi-neun mwo haneun ireul haseyo?*)  
            *Thank you! What do you do, Ji-hoon?*''',

        ''' **지훈:** 저는 회사원이에요. 민준 씨는요?  
            (*Jeoneun hoesawon-ieyo. Minjun-ssi-neunyo?*)  
            *I’m an office worker. How about you?*  ''',

            '''**민준:** 저는 대학생이에요. 지금 경제학을 공부하고 있어요.  
            (*Jeoneun daehaksaeng-ieyo. Jigeum gyeongjehageul gongbuhago isseoyo.*)  
            *I’m a university student. I’m studying economics.*  ''',

            '''**지훈:** 아, 그렇군요. 열심히 공부하세요!  
            (*A, geureokunyo. Yeolsimhi gongbuhaseyo!*)  
            *Oh, I see. Study hard!*  ''',

            '''**민준:** 감사합니다! 다음에 또 이야기해요.  
            (*Gamsahamnida! Daeume tto iyagihaeyo.*)  
            *Thank you! Let’s talk again next time.*  ''']
    conversations = [q_a_response,easy_Phrases,response_]
    opt = st.radio("Pick a list to chat:",name_of_list)
    opt2 = st.radio("Choose to lead or follow in conversation",["Lead","Follow"])
    for i in range(len(name_of_list)):
        if name_of_list[i] == opt:
            some_list = conversations[i]

    lead = []
    follow = []
    for i in range(len(some_list)):
        if i%2 == 0:
            lead.append(some_list[i])
        elif i%2 != 0:
            follow.append(some_list[i]) 
    if 'i' not in st.session_state:
        st.session_state['i'] = 0
    #a = Russian_hash.get("Да")
    #print(type(str(a)))
        # Streamed response emulator
        
    with st.container():
        if st.button("Start a new chat",help="clear chat with new phrases when done"):
            
            st.write('The chat is over.')

            st.cache_data.clear()
            st.cache_resource.clear()
            st.session_state['i'] = 0  
            st.session_state['messages'] = []
            st.rerun()

    def response_generator():
        
        #response = response_[st.session_state.i]
        if opt2 == "Lead":
            response2 = follow[st.session_state['i']]
        else:
            response2 = lead[st.session_state['i']]
        for word in response2.split():
            
            yield word + " " 
            time.sleep(0.15)
        #st.session_state.i += 1




    st.title("Chat")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Say your part then press 'a' to check your answer"):
        
        if opt2 == "Lead":
            response_3:str = lead[st.session_state['i']]
        else:
            follow.insert(0," You start")
            response_3:str = follow[st.session_state['i']]
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt+" : " + response_3})
        # Display user message in chat message container
        
        with st.chat_message("user"):
            st.markdown(prompt + response_3)
        if prompt == 'a':
            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                response = st.write_stream(response_generator())
                
            # Add assistant response to chat history

            
            st.session_state.messages.append({"role": "assistant", "content": response})
            
            st.session_state.i +=1

except(IndexError):
    st.success('The chat is over.')
