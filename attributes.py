"""
Imlement the stack program where Last in first out approch is used.

"""

class Stack:
    name = 0
    numberList = []

    def __init__(self, name):
        self.name = name
        Stack.numberList += 1

        if Stack.numberList <= 5:
            Stack.numberList.append(self)
        else:
            del Stack.numberList[0]
            Stack.numberList.append(self)

    @staticmethod
    def displayStack():
        for numbers in Stack.numberList:
            print(numbers.name, end=' ')
        print()

numberOne = Stack("One")
numberTwo = Stack("Two")
numberThree = Stack("Three")
numberFour = Stack("Four")
numberFive = Stack("Five")
numberFive.displayStack()
numberSix = Stack("Six")
numberSix.displayStack()

