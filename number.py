
import random
secret = random.randint(1,99)
guess = 0
tries = 0
print "Ёй, на палубе! я ”жасный пират –обертс, и у мен€ есть секрет!"
print "Ёто число от 1 до 99. я дам тебе 6 попыток."
while guess != secret and tries < 6:
    guess = input ("“вой вариант?")
    if guess < secret :
        print "Ёто слишком мало, презренный пес!"
    elif guess > secret:
            print "Ёто слишком много, сухопутна€ крыса!"
    tries = tries +1

if guess == secret:
    print "’ватит! “ы угадал мой секрет!"
else:
    print "ѕопытки кончились!"
    print "Ёто число", secret
