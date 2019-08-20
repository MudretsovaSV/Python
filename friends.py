#friends=[]
#friends.append("David")
#friends.append("Mary")
#print friends


letters=["a","b","c","d","e"]
#print type(letters[1])
#print type(letters[1:2])
#print letters[2:]
#print letters[:]
#letters[2]="c"
letters.append("n")
letters.extend(["p","q","r"])
letters.insert(2,"z")
#letters.append(["s","t","u"])
print letters[:]

#letters.remove("c") 
#print letters[:]

#if "a" in letters:
#    print "найден символ a в списке letters"
#else:
 #   print "символ a в списке letters не обнаружен"
#if "a" in letters:
 #   letters.remove("a")

#del letters[3]
#print letters[:]

#lastLetter=letters.pop()
#print letters
#print lastLetter
#second=letters.pop(1)
#print second
#print letters
letters.sort()
print letters
letters.sort(revers=True)
print letters[:]
