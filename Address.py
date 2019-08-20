import easygui
index=str(easygui.enterbox(" Enter your index: "))
country=str(easygui.enterbox(" Enter your country: "))
city=str(easygui.enterbox(" Enter your city: "))
street=str(easygui.enterbox(" Enter your street: "))
HomeNumber=str(easygui.enterbox(" Enter your HomeNumber: "))
ApartmentNumber=str(easygui.enterbox(" Enter your Apartment Number: "))
Name=str(easygui.enterbox(" Enter your Name: "))

easygui.msgbox("Your address is: " + index + country+','+ city
               + street + HomeNumber + ApartmentNumber
               + Name )

