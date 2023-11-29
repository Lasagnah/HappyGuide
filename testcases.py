from main import *

def TestCase1():
    h = helper()
    h.head.getTasks()

def TestCase2():
    h = helper()
    h.head.updateTask("test HappyGuide", True)
    h.head.getTasks()

def TestCase3():
    h = helper()
    h.addDaily("Get up out of bed")
    h.addDaily("orange")
    h.removeDaily("orange")
    h.advance()
    h.head.getTasks()

print("Test Case 1:")
TestCase1()
#configure HappyGuide : incomplete
print("Test Case 2:")
TestCase2()
#configure HappyGuide : incomplete
#test HappyGuide : completed
print("Test Case 3:")
TestCase3()
#Get up out of bed : incomplete