def printMyAddress():
    print "Warren Sande"
    print "123 Main Street"
    print "Ottawa, Ontario, Canada"
    print "K2M 2E9"
    print

#printMyAddress()

def printMyAddress(myName):
    print myName
    print "123 Main Street"
    print "Ottawa, Ontario, Canada"
    print "K2M 2E9"
    print

#printMyAddress("Warren Sande")
#printMyAddress("Karter Sande")

def printMyAddress(someName,houseNum):
    print someName
    print houseNum, "Main Street"
    print "Ottawa, Ontario, Canada"
    print "K2M 2E9"
    print

#printMyAddress("Warren Sande","45")
#printMyAddress("Karter Sande", "64")

#def scalculateTax(price, tax_rate):
 #   taxTotal=price+(price*tax_rate)
 #   return taxTotal

#totalPrice=calculateTax(7.99,0.06)
#print totalPrice
#print calculateTax(7.99,0.06)+calculateTax(6.59,0.08)



def calculateTax(price, tax_rate):
    total=price+(price*tax_rate)
   # my_price=1000
 #   global my_price
   
   # print my_price 
 #   return total

my_price=float(raw_input("Vvedite cenu: "))

totalPrice=calculateTax(my_price,0.06)
print  "cena=", my_price, "Itogovaya cena=", totalPrice



