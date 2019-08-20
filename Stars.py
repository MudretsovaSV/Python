#numStars=int(raw_input("Сколько звезд вам нужно?"))
#for i in range(0,numStars):
#    print '*',

numBlocks=int(raw_input("Сколько блоков звезд вам нужно?"))

#numLines=int(raw_input("Сколько строк в каждом блоке?"))
#numStars=int(raw_input("Сколько звезд должно быть в строке?"))

for block in range(1,numBlocks+1):
    print 'блок = ', block
    for line in range(1,block*2):

#    for line in range(0,numLines):
#        for star in range(0,numStars):

        for star in range(1,(block+line)*2):
            print '*',
        print "строка = ", line, "звезд = ", star
    print
