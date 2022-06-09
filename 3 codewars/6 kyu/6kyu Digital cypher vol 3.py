'''
https://www.codewars.com/kata/digital-cypher-vol-3-missing-key/train/python
 s  c  o  u  t
  19  3 15 21 20
 + 1  9  3  9  1
 ---------------
  20 12 18 30 21

   m  a  s  t  e  r  p  i  e  c  e
  13  1 19 20  5 18 16  9  5  3  5
+  1  9  3  9  1  9  3  9  1  9  3
  --------------------------------
  14 10 22 29  6 27 19 18  6  12 8
'''
print(''.join(map(chr, range(97, 123))))
message,code = "scout", [20, 12, 18, 30, 21]
message,code = "nomoretears", [15, 17, 14, 17, 19, 7, 21, 7, 2, 20, 20]
#message,code = "masterpiece",[14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]
def find_the_key(message, code):
    re,res,gap,alpha = [],[],[],''.join(map(chr, range(97, 123)))
    for e in message:
        for i,f in enumerate(alpha):
            if e == f:
                re.append(i+1)
    quot,rem = len(message)//len(code),len(message)%len(code)
    code_dup = code * quot + code[0:rem]

    for i in range(len(re)):
        res.append(code_dup[i] - re[i])
    return res
res = find_the_key(message, code)

def key(res):
    i,j = 0,1
    while i < len(res) and j <= len(res):
        if res[j] == res[i]:
            i += 1
            j += 1

        elif res[j] != res[i]:
            j += 1
        return res[i:j]



print(find_the_key(message, code))
print(key(res))

'''
list(map(lambda x = i+j,[i for i in message],[i for i in code_dup]))
        if res[0] == res[x]:
            if x*2+1 < len(res):
                if res[:x] == res[x:x*2]:
                    return int(''.join(str(i) for i in res[:x]))
            elif x*2+1 > len(res):
                return int(''.join(str(i) for i in res[:x]))
********************************   b***************************************  
        for gap in range(len(code),0,-1):
            if i+gap < len(res) and res[i] == res[i+gap]:
                return gap
                
 *******************************************                 
                
    st = len(res)//2
    print(st,len(res),res)
    for i in range(st+1):
        #print(i)
        print(res[0:st - i+1], res[st + i:])
        #while st - i > 0 and st + i < len(res):
        if res[0:st-i] == res[st+i:]:
            print(res[0:st-i],res[st+i:])
            gap.append(i)
            print(gap)
    return int(''.join(str(i) for i in res[:gap[-1]])) 
    
    
        if res[:st-i] == res[st-i:2*(st-i)]:
            print(res[:st-i],res[st-i:2*(st-i)])
    
        st,i = len(res)//2,0
    for i in range(len(res)):
        print(res[:st-i],res[st-i:2*(st-i)])
        if res[:st-i] == res[st-i:2*(st-i)] and len(res[:st-i])%2 == 0:
            return key(res[:st-i])
        elif res[:st-i] != res[st-i:2*(st-i)] or len(res[:st-i])%2 == 1:
            return res[:st-i]              
'''