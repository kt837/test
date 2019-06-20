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

def testSucs():
    print("Congratulations, have a nice day!")

def checkAnswer():
    answer = input()
    if answer == 2:
        testSucs()
    else:
        print("Please, try again.")
        checkAnswer()

def testing():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times." + "\n" + "2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program." + "\n" + "4. To interrupt the execution of a program.")
    print("Your answer: ")
    checkAnswer()
