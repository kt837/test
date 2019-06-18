"""
Personal Curriculum project

06.18.19 L340E

"""

def guessage():
    print("Say me remainders of dividing your age by 3, 5 and 7.")
    myage3 = input()
    myage5 = input()
    myage7 = input()
    age = (myage3  * 70 + myage5 * 21 + myage7 * 15) % 105
    return age

def Greatings():
    assistantname = "Veston"
    birthYear = 1995
        
    print("Hello! My name is " + assistantname)
    print("I was born in " + str(birthYear))
    print("Please, remind me your name.")
    myname = input()
    print("What is a great name, " + myname)
    print("Let's me guess your age.")
    myage = guessage()
    print("Your age is " + str(myage) +"; that's a good time to start programming!")
    
def counting():
    print("Now I will prove to you that I can count to any number you want.")
    count = input()

    for i in range(0, count + 1):
        print(str(i) + "!")
    print("Completed, have a nice day!")

