
from translate import Translator

# 以下是将简单句子从英语翻译中文
translator= Translator(to_lang="chinese")
translation = translator.translate("Good night!")
print(translation)

# 在任何两种语言之间，中文翻译成英文
translator= Translator(from_lang="chinese",to_lang="english")
translation = translator.translate("我想你")
print(translation)

translator= Translator(from_lang="chinese",to_lang="french")
translation = translator.translate("我想你")
print(translation)


# 在任何两种语言之间，中文翻译成英文
translator= Translator(from_lang="chinese",to_lang="english")
translation = translator.translate("我爱你")
print(translation)

translator= Translator(from_lang="chinese",to_lang="french")
translation = translator.translate("我爱你")
print(translation)