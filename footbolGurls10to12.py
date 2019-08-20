gender=raw_input("Ваш пол - m или f? (m-мужской, f-женский) ")
if gender=="m":
    print "Вы не подходите."
elif gender=="f":
    age=float(raw_input("Сколько Вам лет? "))
    if 10<=age<=12:
        print "Вы подходите"
    else: print "Вы не подходите"
