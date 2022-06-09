import jieba
from stylecloud import gen_stylecloud

def cloud(file_name):
    with open(file_name, 'r', encoding='utf8') as f:
        word_list = jieba.cut(f.read())
        result = " ".join(word_list)  # 分词用 隔开
        # 制作中文云词
        gen_stylecloud(text=result,
                       font_path='C:\\Windows\\Fonts\\simhei.ttf',
                       palette='cartocolors.diverging.Fall_4',
                       icon_name='fas fa-car',
                       output_name='t4.png',
                       )  # 必须加中文字体，否则格式错误


if __name__ == "__main__":
    file_name = './word.txt'
    cloud(file_name)


from stylecloud import gen_stylecloud
gen_stylecloud(file_path='Trump.txt')