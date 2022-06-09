'''
https://www.codewars.com/kata/5a145ab08ba9148dd6000094/train/python
'''

#1st solution
def doubles(s):
    cs = []
    for c in s:
        if cs and cs[-1] == c:
            cs.pop()
        else:
            cs.append(c)
    return ''.join(cs)

#2nd solution

import re
def doubles(s):
    re_double = re.compile(r'(.)\1')
    while re_double.search(s):
        s = re_double.sub('', s)
    return s



from collections import deque
s = 'xxbnnnnnyaaaaam'
#s = 'gfuxbrfetlkrlqhjwtmzdeaulzrsxxfalyasoqshrtrlbebyhwqrotgwydsbcsqvetwxcsrcgkhcwsdxeatxlrbacmpcybqdnoauainurocedawdjhwvztlriqigesmljawdymetzdqlgtpsfydemmreeaiqmzuhmpntiyzfghytogdxrhxbznfvlnusbxmwuijiiclygqyapwzswibqxldksovxzoqyabhwdsmljjcnhkvcmpvcyutorvjvuvilufhnflcdhazcsqlwnrgikaxkcsructcrhtnwalephnhcznxmzwrdmfitkjiqezryctswbobrvauwnmfytcukpmqkwkiemgslpcltlrlpjyblvegfuynlrukpzjmukbwvyvtlnmxjfizzqdckeuevzphevhmfebutlwvurzblvfeyftjdakrokoimluvshclilqbgbqtjigpbwzmmuzzhenboadihllqjsipdcfuxtufwyshzbsiuvszyieebnhlhlyowxetsanietrqoteogynapxgqjdonzptwhioaedsutdbfatvokzmwfdlnasdvgapikagybkfpmoalwewpxndntjkbhiuyvjmkfbdpjqdootwhltiwqitpykwkzlxwnwfozxodiecfeuhywtwgmgaqscshugyvlsnmbyavbnkvmfitikgbrhdxakhevinzbxtfagfcjgenidrftykgwxwgevuskwvnmqsvkqmpmaxfxmudbqsrqjhtzqmchnsgkhkffbmcapvzfmopbevtxjdrojwnqidoinnaztyvmzblggwcibaqcpwrysbktwcrftjewkadskcwyevozriktxztsvzhajgufdidjqcmjmpelykapxzftkfbhoijauzxrfbozulbnmciodupvsmwlmtecpzlkhyhfvgamhisihsmeosgauplsuhultvifnsvwgvtdveactqhjwzaiorxktauqvuwbvtcezxkjvmvfcalypipequldpmasrljuthfqmdlyxgpgwyeluvwrtkdlxnuxzlddmjwmrgmrluxskqoxlhicohjgeahwedbgajhtuvifdbsavuifaqqjkvwdghdnqtgvoqreftqsnvibjdboygrxnmtfxekfoabnwgcnlhyfvtdxrhqvcmizwyzkolbminqgvevujsamqbxpnlcfplxjhcdpntbbjqdhvdrbijajonqzokiqarpqztwfykauvcgribhzsijoetrwrrxkmewdrsosbwubgjcvpmfzebyeydigygmsdctfewzzltbuszvbzyfotwobtmjocaiubgsafvgocpfnwivieojrnsqlfbfaogqgpwtdhumrfqfctaeyomsmaewhtlybtgstfyevhrwsfsxpsuhlhkcjcvygjuzgreoprkeykqaeyzagjnayvoxmnsejedtksiwqbbnkvdpisfcrpljpblpmczykuqdcxsrqlmnpbdcnjzxztdkqfaqdqisjfivwfjdgcfakpeogwptwdwvnkxvdhzmwebmetiwzjfylbaxjevowilzicivjdtyirqvzqnbjzvrjmdvnlinzpruebntgskwuwuctyomwrpcphqkbowvuzgonmojplluxsxichfkaqjglfitrgewwwntsnmjgcbjhrykyxvhqlfcbvtoxbgpkqxftnjabnewpvihzzgzqrkqvziosywdycojybuytiqdvaawhpbrpgpfabpdhghuchbjrxooxprhsmgofpyzhwulkosktwmhqriaccfyovxvqyxnpifyzkqtrcxiqbtmirjyvokroakegnpxojyoevrvogovigthtavwcnjxqthckcfrbrgxsuypfgyyxokrjcdmvhxsrwabykvzloysyvibamkwmzxzsemkgksrpcyzhbqxoduefajqwonkpidupexkrpfpwklivsjyveawxlhnnbypbsxyrldubueczzudvhlcnfzojlcdivwiuygwkwgctkypntnywjoqjpxzewssgogwnydabnsvmaruzvrdcftsuepxalbunuzifdvtgpwfsbeqbbqadfkvwufcszmnbfrjtprvhixubkcnptghhgxdfewtobniusvanfvfplqdvtnhzsrpmegzxjhygwipvjckjfuaetlufdmpcjpqtjmfslvrerlduymylsiqwlharpivqsiuzglwuthycivuysurnjjxeaibwkqxmanckpwcvpihprxnjgutfgytozwtdgpojtoybwpifrzglgqnkazmwfyumuenszwzyhehmxvyfvpexfxoehsmkuzayxejyuwnynvdxnutisgpxaldqaeyxfalmduvjcnadmzvlefbktwhodwaevyhgfzhkqzvdwyvhobvtvrynqylirvsczqiivycpsiplipkqdsr'
sq = deque(s)
sq.popleft()
sq.popleft()
n = sq.popleft()
print(sq,n)


def doubles(s):
    i,s = 0,s+'  '
    ans = ''
    sq = deque(s)
    while len(deque(sq)) > 0:

        if sq[0] == ' ':
            return ans
        elif sq[0] == sq[1]:
            sq.popleft()
            sq.popleft()
            i += 2
            print(sq)
        elif sq[0] != sq[1]:
            ans += sq.popleft()
            ans += sq.popleft()

print(doubles(s))



def doubles(s):
    sl = list(s)
    i = 0
    while i < len(sl)-1:
        if sl[i] == sl[i+1]:
            sl[i] = 0
            sl[i + 1] = 0
            i += 2
        else:
            i += 1
    return ''.join([i for i in sl if i != 0])
print(doubles(s))