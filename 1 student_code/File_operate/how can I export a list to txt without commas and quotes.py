
fruits = ['bananas', 'apples', 'oranges', 'strawberry']
with open("fruits_text.txt", 'w') as totxt_file:
    totxt_file.write(str(fruits)+'\n')


fruits = ['bananas', 'apples', 'oranges', 'strawberry']
with open("fruits_text.txt", 'w') as totxt_file:
    for fruit in fruits:
        totxt_file.write(fruit + '\n')