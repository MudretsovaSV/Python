#class GameObject:
  #  def __init__(self,name):
 #       self.name=name
#
   # def pickUp(self,player):
  #      pass
 #   
#class Coin(GameObject):
  #  def __init__(self,value):
 #       GameObject.__init__(self,"monetka")
   #     self.value=value

   # def spend(self,buyer,seller):
  #      pass
#-------------------------------------------------------------------------
class BankAccount:
    def __init__(self,name,Nscheta):
        self.name=name
        self.Nscheta=Nscheta
        self.schet=0
        self.data=[]

    def __str__(self):
        S=str(self.schet)
        msg="Sostoyanie scheta "+ S +" rub."
        return msg
        
      
    def AddorSnyat(self,s,summa):
        self.data.append(data)
        if s=="A":
            self.schet=self.schet+summa
        elif s=="S":
            self.schet=self.schet-summa
        return self.schet

class InterestAccount(BankAccount):
    def __init__(self,Stavka):
        BankAccount.__init__(self)
        self.Stavka=Stavka
        
    def __str__(self):
        S=str(self.schet)
        d=self.data
        msg="Sostoyanie scheta "+ S +" rub."+" cleduyushaia data spisaniya "+ d
        return msg
                
    def addInterest(self):
        self.schet=self.schet+self.schet*self.Stavka/100.0
        self.data.append(newdata)
        return self.schet, self.data
    
data=raw_input("Data GGGG.MM.DD: ")
name=str(raw_input("Vashe Imya: "))
Nscheta=float(raw_input("Nomer scheta: "))
mySchet=BankAccount(name,Nscheta)
print mySchet
s=raw_input("Vi hotite popolnit schet ili snyat? A/S ")
summa=float(raw_input("Summa popolneniya/snyatiya: "))
print "Sostoyanie scheta ", mySchet.AddorSnyat(s,summa)
Stavka=float(raw_input("Vvedite stavku: "))
newdata=raw_input("Vvedite sledushuyu Datu nachisleniya procentov GGGG.MM.DD: ")
addInterest(Stavka)


