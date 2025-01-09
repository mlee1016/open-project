
from Every_korean_ph import korean_useful_polite_words
def __main__():



    definition = ['water', 'bill', 'please', 'hello', 'its okay', 'how much is it', 'a little', 'sorry', 'where is it', 'toilet', 'slowly', 'photo', 'what is it', 'tell me', 'card', 'korean', 'cant', 'thank you', 'number', 'menu', 'okay', 'byeolyo', 'one', 'there is', 'tell me', 'time', 'this', 'take a picture', 'here', 'help me', 'again', 'next time', 'name', 'well', 'its delicious']
    romitization = ['''dasi,
dwaeyo,
igeo,
bwaeyo,
jjig-eodo,
da-eum-e,
juseyo,
jom,
sigan-i,
joesonghabnida,
malsseumhae,
dowajuseyo,
mas-iss-eoyo,
menyu,
moshaeyo,
yeogiyo,
igeo,
kadeu,
iss-eoyo,
malhae,
hwajangsil-i,
jjig-eodo,
mul,
eolmayeyo,
juseyo,
gwaenchanh-ayo,
da-eum-e,
hangugmal,
eodiyeyo,
bwaeyo,
mwoyeyo,
jal,
gyesanseo,
sajin,
annyeonghaseyo
dasi,
han,
ileum-i,
beon,
dwaeyo,
gamsahabnida,
cheoncheonhi,
''']
    ro = romitization[0].split("\n")
    for i in range(len(korean_useful_polite_words)):

        print("'",list(korean_useful_polite_words)[i],"'",",")





if __name__ == "__main__":
    __main__()