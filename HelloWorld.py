import sys

def sayHello():
    helloArray = ["H", "e", "l", "l", "o", "w", "o", "r", "l", "d", "!"]
    for letterIndex in range(len(helloArray)):
        if letterIndex == 5:
            sys.stdout.write(" ")
        sys.stdout.write(helloArray[letterIndex])

sayHello()
