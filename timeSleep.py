sec=int(raw_input("Таймер обратного отсчета: Сколько секунд? "))
import time
for i in range(sec,0,-1):
    print i, "*"*i
    time.sleep(1)
print "Пуск!"
