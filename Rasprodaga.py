price=float(raw_input("Какова цена товара? "))
if price<=10:
    priceWithDiscount1=price*0.9
    print "Ваша скидка 10%. Итоговая цена:", priceWithDiscount1
elif price>10:
    priceWithDiscount2=price*0.8
    print "Ваша скидка 20%. Итоговая цена:", priceWithDiscount2
