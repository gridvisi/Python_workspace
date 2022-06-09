'''
https://www.codewars.com/kata/59d2fc6c23dacca182000068/train/python
在西方音乐中，大调和弦（大三度）从一个根音开始，在它上面加上4个半音和7个半音。
小和弦(小三度)从一个音符开始，在它上面加上3个半音和7个半音。
给定一个音符根音，请返回该根音的大和弦和小和弦的数组。
这些音符是C, C#, D, D#, E, F, F#, G, G#, A, A#, B -- 你得到的是一个常数。

In Western music, a major chord (major third) starts at a root note and adds the note
4 semitones and 7 semitones above it.

A minor chord (minor third) starts at a root note and adds the note 3 semitones and
7 semitones above it.

Given a root note root, please return an array of the major chord and the minor chord
for that root.

The notes are C, C#, D, D#, E, F, F#, G, G#, A, A#, B –– you are given this as a constant

'''

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def chords(root):
  # your code here
  return [major, minor]