import easygui
f=float(easygui.enterbox(""" This program converts Fahrenheit degrees to Celsius degrees.
Enter degrees fahrenheit """))
c=(f-32)*5.0/9
easygui.msgbox("It's "+str(c) + " degrees Celsius")
