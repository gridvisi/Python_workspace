
#删除一些感叹号以使每个感叹号的开头和结尾保持相同的感叹号数目
def remove(s):
    s = s.split(' ')
    left = 0
    right = 0
    output_count = 0
    cam = 0
    for i in range(0,len(s)):
        temp = list(''.join(s[i]))
        for j in temp:
            if j == '!' and cam == 0:
                left += 1
            elif j == 'H' and cam == 0:
                continue
            elif j == 'i' and cam == 0:
                cam = 1
                continue
            elif j == '!' and cam == 1:
                right += 1
    if left > right: output_count = right
    elif right < left: output_count = left
    else: output_count = right
    for i in range(0,len(s)):
        temp = ''
        for i in range(output_count):
            temp += '!'

print(remove("!!Hi! Hi!"))