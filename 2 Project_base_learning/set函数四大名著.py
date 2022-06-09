famous_4 = F4 = ["水浒传","三国演义","西游记","红楼梦"]
ada_book = ["三国演义","西游记","红楼梦"]
feifei_book = ["水浒传","西游记","红楼梦"]

print(set(ada_book) & set(feifei_book))
print(set(ada_book) | set(feifei_book))
print(set(ada_book) - set(feifei_book))
print(set(feifei_book) - set(ada_book))