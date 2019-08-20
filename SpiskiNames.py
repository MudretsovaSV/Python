names=[]
print "Vvedite 5 imen(posle kagdogo nagimaite Enter: "
names.append(raw_input())
names.append(raw_input())
names.append(raw_input())
names.append(raw_input())
names.append(raw_input())
print "Eto imena: ", 
for n in names:
    print n,
print
#print "--------------------------------"
#new=sorted(names)
#for s in new:
#    print s,
#print
print "--------------------------------"
print "Tretie vvedennoe vami imya: ", names[2]
name=raw_input("Kakoe imya nugno zamenit? ")
if name in names:
   names[names.index(name) ]=raw_input("novoe imya: ")
print "Eto imena: ", 
for n in names:
    print n,
print
