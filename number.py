
import random
secret = random.randint(1,99)
guess = 0
tries = 0
print "��, �� ������! � ������� ����� �������, � � ���� ���� ������!"
print "��� ����� �� 1 �� 99. � ��� ���� 6 �������."
while guess != secret and tries < 6:
    guess = input ("���� �������?")
    if guess < secret :
        print "��� ������� ����, ���������� ���!"
    elif guess > secret:
            print "��� ������� �����, ���������� �����!"
    tries = tries +1

if guess == secret:
    print "������! �� ������ ��� ������!"
else:
    print "������� ���������!"
    print "��� �����", secret
