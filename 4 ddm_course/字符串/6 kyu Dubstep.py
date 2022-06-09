# https://www.codewars.com/kata/551dc350bf4e526099000ae5/train/python
'''
Polycarpus works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance. Recently, he has decided to take a couple of old songs and make dubstep remixes from them.
Let's assume that a song consists of some number of words (that don't contain WUB). To make the dubstep remix of this song, Polycarpus inserts a certain number of words "WUB" before the first word of the song (the number may be zero), after the last word (the number may be zero), and between words (at least one between any pair of neighbouring words), and then the boy glues together all the words, including "WUB", in one string and plays the song at the club.
For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX".
Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, he decided to find out what was the initial song that Polycarpus remixed. Help Jonny restore the original song.
Input
The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters

Output
Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.

Polycarpus在最好的Berland夜总会担任DJ，他经常在表演中使用dubstep音乐。最近，他决定把几首老歌从中进行dubstep混音。

假设一首歌由一些词组成（不包含WUB）。为了制作这首歌的dubstep混音，波利卡普斯在歌曲的第一个词前（数量可以是零）、最后一个词后（数量可以是零）、词与词之间（任意一对相邻词之间至少有一个）插入一定数量的词 "WUB"，然后男孩将包括 "WUB "在内的所有词粘合成一串，在俱乐部播放这首歌。
例如，一首带有 "I AM X "字样的歌曲，在dubstep混音中可以转化为 "WUBWUBIWUBAMWUBWUBX"，而不能转化为 "WUBWUBIAMWUBX"。
最近，Jonny听到了Polycarpus的新dubstep歌曲，但由于他不喜欢现代音乐，所以他决定找出Polycarpus混音的最初歌曲是什么。帮助Jonny还原原曲。

输入由单个非空字符串组成，仅由大写英文字母组成，字符串的长度不超过200个字符。
output: 返回Polycarpus用来制作dubsteb混音的初始歌曲的词。用空格分隔歌词。
'''
song = "AWUBWUBWUBBWUBWUBWUBCWUB"  
print(song.replace('WUB', ' '))
print(song.replace('WUB', ' ').split())

def song_decoder(song):
    #s = song.replace('WUB','-')
    #print(song.split('WUB'))
    return ''.join([f"{i}{' '}" for i in song.split('WUB') if i.isalpha()])[:-1]

#1st solution
def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())

def song_decoder(song):
    import re
    return re.sub('(WUB)+', ' ', song).strip()

def song_decoder(song):
    return ' '.join([a for a in song.split('WUB') if a])

import re
def song_decoder(song):
    return re.sub(r'(WUB)+', ' ', song).strip()

def song_decoder(song):
    """ Simple WUB decoder :) """

    # Splitting strings by "WUBs" and filtering out voids
    list = filter(lambda x: x != '', song.split('WUB'))

    # Returning the joint items separed by spaces
    return ' '.join(list)

def song_decoder(song):
    return ' '.join(filter(None, song.split('WUB')))

def song_decoder(song):
    return ' '.join(word for word in song.split('WUB') if word)

def song_decoder(song):
    a = song.split('WUB')
    a = ' '.join(a)
    a = a.split()
    return ' '.join(a)



#'R---L-' should equal 'R L'
#'-JKD--WBIRAQKF--YE---WV--' should equal 'JKD WBIRAQKF YE WV'
#'-KSDHEMIXUJ--R---S---H---' should equal 'KSDHEMIXUJ R S H'
song = "AWUBWUBWUBBWUBWUBWUBC"
#song = "WUBAWUBBWUBCWUB"
#song = '-JKD--WBIRAQKF--YE---WV--'
print(song_decoder(song))

def song_decoder(song,ans=[]):
    s = song.replace('WUB','-')
    #print(ans)
    i, j = 0, 1
    while i < j < len(s):
        if i == 0 and set(list(s[i:j])) == {'-'}:
            j += 1
        ans.append(s[j-1])
        s = s[j:]
        if len(s) < 2:
            return  ans #' '.join(''.join(ans).split('-'))
        return song_decoder(s)
