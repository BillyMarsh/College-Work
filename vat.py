def vatStuff(name,price):
    vat = price * 0.2
    price = price + vat
    print(name, "£",price)


vatStuff("teabags",10)
