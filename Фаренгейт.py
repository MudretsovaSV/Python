import easygui
print "��� ��������� ����������� ������� ���������� � ������� �������"
# print "������� ����������� � �������� ����������: ",
f=float(easygui.enterbox("Enter degrees fahrenheit "))
# f=float(raw_input())
c=(f-32)*5.0/9
print "��� ",
print c, "�������� �������"
easygui.msgbox("It's "+str(c) + " degrees Celsius")
