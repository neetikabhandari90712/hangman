import time
import random

secret_word = ["misplace","doll","dog","panda","tiger","mohit","himalayas","tree","ghost","goverment","hydrogen"]
word = random.choice(secret_word)
length = len (word)

name = input("Hey , Can i know your name please :")
print("HELLO :)  "+ name +"come on lets play HANGMAN " )
time.sleep(1)
print("LETS START")
time.sleep(0.5)
print()

life = input("How many lives do you want :")
count = 0
display = "#"*length
limit = int(life)


def hangman(count, display, word):

    guess = input("This is Word:" + display + "Enter your guess:")
    if guess in word:
        index = word.find(guess)
        word = word[:index]+"*"+word[index+1:]
        display = display[:index]+guess+display[index+1:]
    else:
        count += 1

        if int(count) <= int(limit):
            sub = limit - count
            print("wrong input {} guess remaining".format(sub))

    if word == "#" * length:
        print("Congratulations")
    elif count != limit:
        hangman(count, display, word)


hangman(count, display, word)
