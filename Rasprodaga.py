price=float(raw_input("������ ���� ������? "))
if price<=10:
    priceWithDiscount1=price*0.9
    print "���� ������ 10%. �������� ����:", priceWithDiscount1
elif price>10:
    priceWithDiscount2=price*0.8
    print "���� ������ 20%. �������� ����:", priceWithDiscount2
