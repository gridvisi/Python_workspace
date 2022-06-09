with open('dict.txt') as f:
    lines = f.read()
reverse_dict = {}

for line in lines.split("\n"):
    en_word, es_words = line.split(" ", 1)
    for es_word in es_words.split(","):
        if es_word not in reverse_dict:
            reverse_dict[es_word] = []
        reverse_dict[es_word].append(en_word)

for es_word, en_words in reverse_dict.items():
    if len(en_words) > 1:
        en_words = ",".join(en_words)
        print(f"{es_word}: {en_words}")