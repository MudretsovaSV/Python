import easygui
print "Эта программа преобразует градусы Фаренгейта в градусы Цельсия"
# print "Введите температуру в градусах Фаренгейта: ",
f=float(easygui.enterbox("Enter degrees fahrenheit "))
# f=float(raw_input())
c=(f-32)*5.0/9
print "Это ",
print c, "градусов Цельсия"
easygui.msgbox("It's "+str(c) + " degrees Celsius")
