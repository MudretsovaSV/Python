#numStars=int(raw_input("������� ����� ��� �����?"))
#for i in range(0,numStars):
#    print '*',

numBlocks=int(raw_input("������� ������ ����� ��� �����?"))

#numLines=int(raw_input("������� ����� � ������ �����?"))
#numStars=int(raw_input("������� ����� ������ ���� � ������?"))

for block in range(1,numBlocks+1):
    print '���� = ', block
    for line in range(1,block*2):

#    for line in range(0,numLines):
#        for star in range(0,numStars):

        for star in range(1,(block+line)*2):
            print '*',
        print "������ = ", line, "����� = ", star
    print
