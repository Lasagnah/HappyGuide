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
    h.advance()
    h.head.getTasks()

print("Test Case 1:")
TestCase1()
print("Test Case 2:")
TestCase2()
print("Test Case 3:")
TestCase3()