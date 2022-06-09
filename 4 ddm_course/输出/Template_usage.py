

from string import Template
def main():
    cart = []
    cart.append(dict(item='coke',price=11,qty= 1))
    cart.append(dict(item='cake',price=12,qty=6))
    cart.append(dict(item='fish',price = 1,qty =4))

    t = Template("$qty * $item = $price")
    total = 0
    print("Cart")
    for data in cart:
        print(t.substitute(data))
        total += data["price"]

    print("Total: %s"%(total,))

if __name__ == "__main__":
    main()

main()


#1

from string import Template
s = Template("there are ${how_many} ${lang} student in ${school}")
print(s.substitute(lang='Python',how_many=30,school = 'ddm_coding_camp'))
#there are 3  Python Quotation symbols