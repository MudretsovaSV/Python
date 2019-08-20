x=int(raw_input("Для какого числа нужна таблица умножения? "))
k=int(raw_input('До какого множителя вы хотите дойти? '))   
print ("Вот Ваша таблица:")
#for i in range(1,11):
i=1
while i!=k+1:
    print i, " x ",x,"= ",i*x
    i=i+1 
