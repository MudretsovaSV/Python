#letters=['d','a','e','c','b']
#print letters
#letters.sort()
#print letters
#letters.reverse()

#letters.sort(reverse=True)
#print letters


original_list=["Tom","Jams",'Sara','Fred']
new_list=original_list[:]
new_list.sort()
print original_list
print new_list


original=[5,2,3,1,4]
newer=sorted(original)
print original
print newer

my_tuple=("red",'green','blue')
print my_tuple

JoeMarks=[55,63,77,81]
TomMarks=[65,61,67,72]
BethMarks=[97,95,92,88]

mathMarks=[55,65,97]
scienceMarks=[63,61,95]
readingMarks=[77,67,92]
spellingMarks=[81,72,88]

classMarks=[JoeMarks,TomMarks,BethMarks]
print classMarks

classMarks=[[55,63,77,81],[65,61,67,72],[97,95,92,88]]
print classMarks

for studentsMarks in classMarks:
    print studentsMarks

print classMarks[0][2]



