import easygui
pin=easygui.enterbox("Введите пароль ")
if pin=="Молодец!":
    easygui.msgbox("Вот вы и вошли!")
else: easygui.msgbox("Пароль не верный") 
