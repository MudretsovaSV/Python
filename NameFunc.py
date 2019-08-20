def name():
   print " "*2+"C"*4+" "*7+'A'+" "*6+'R'*5+" "*2+'T'*7+" "+'E'*6+" "+'R'*5
   print " "+'C'+" "*4+'C'+" "*5+'A'+" "+'A'+" "*5+'R'+" "*4+'R'+" "*4+'T'+" "*4+'E'+" "*6+'R'+" "*4+'R'
   print 'C'+" "*10+'A'+" "*3+'A'+" "*4+'R'+" "*4+"R"+" "*4+'T'+" "*4+'E'*4+" "*3+'R'+" "*4+'R'
   print 'C'+" "*9+'A'*7+" "*3+'R'*5+" "*5+'T'+" "*4+'E'+" "*6+'R'*5
   print " "*1+'C'+" "*4+'C'+" "*2+'A'+" "*7+'A'+" "*2+'R'+" "*4+'R'+" "*4+'T'+" "*4+'E'+" "*6+'R'+" "*4+'R'
   print " "*2+'C'*4+" "*2+'A'+" "*9+'A'+" "+'R'+" "*5+'R'+" "*3+'T'+" "*4+'E'*6+" "+'R'+" "*5+'R'
   print

name()
#name()
   
def address(name,Nflat,Nhome,street,city,index,country):
    print name
    print country,city,index
    print street, " Street ",Nhome, " Flat ¹",Nflat
    

#name=raw_input("Vashe imya: ")
#country=raw_input("Vasha strana: ")
#city=raw_input("Vash gorod: ")
#street=raw_input("Ulica: ")
#Nhome=raw_input("Nomer doma: ")
#Nflat=raw_input("Nomer kvartiri: ")
#index=raw_input("Vash index: ")

# address(name,Nflat,Nhome,street,city,index,country)

def Money(One,Five,Ten,Fifty):
    Itogo=float(0.01*One+0.05*Five+0.1*Ten+0.5*Fifty)
    print "Vsego u nas ", Itogo, "rub."
    print

One=float(raw_input("Monet po 1 kopeike: "))
Five=float(raw_input("Monet po 5 kopeek: "))
Ten=float(raw_input("Monet po 10 kopeek: "))
Fifty=float(raw_input("Monet po 50 kopeek: "))

Money(One,Five,Ten,Fifty)
