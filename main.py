class day:
    num = 0
    def __init__(self):
        self.tasks = helper.daily.copy()
        self.num = day.num
        day.num += 1
        self.next = None
    
    def addTask(self, task):
        if task not in self.tasks.keys():
            self.tasks[task] = "incomplete"

    def completeTask(self, task):
        if task in self.tasks.keys():
            self.tasks[task] = "completed"

    def updateTask(self, task, complete = False):
        if task in self.tasks.keys():
            if complete:
                self.tasks[task] = "completed"
            else:
                self.tasks[task] = "incomplete"
        else:
            #If task not present, add it and check for commpleteness
            self.addTask(task)
            if complete:
                self.completeTask(task)

    def setNext(self, next1):
        self.next = next1

    def getTasks(self):
        #print(self.tasks)
        for i in self.tasks:
            print (i, ":", self.tasks[i])

class helper:
    #This class is basically a linked list with our day objects as our nodes
    #Think of our tasks as being the node's data and it should make more sense
    ratings = []
    #Daily tasks
    daily = {}

    def __init__(self):
        self.head = day()
        self.head.addTask("configure HappyGuide")

    def next(self):
        if self.head.next is None:
            self.head.next = day()

    def advance(self):
        self.next()
        self.head = self.head.next

    @staticmethod
    def addDaily(task):
        helper.daily[task] = "incomplete"

    @staticmethod
    def removeDaily(task):
        if task in helper.daily:
            del helper.daily[task]

    @staticmethod
    def getDaily(task):
        for i in helper.daily:
            print(i)

def mainLoop():
    h = helper()
    while True:
        s = input("d to get info on today, c to update today's tasks, t to get add tasks to tomorrow, a to advance to tomorrow, o to edit daily tasks, x to exit\n")
        if s == "c":
            t = input("what task would you like to update\n")
            b = input("t for completed, f for incomplete\n")
            if b == "t":
                h.head.updateTask(t, True)
            else:
                h.head.updateTask(t, False)
        elif s == "d":
            h.head.getTasks()
        elif s == "o":

            while True:
                s = input("r to remove a daily task, p to print daily tasks, a to add a daily task, x to go back")
                if s == "r":
                    s = input("what task would you like to remove\n")
                    helper.removeDaily(s)
                elif s == "p":
                    helper.getDaily()
                elif s == "a":
                    s = input("what task would you like to add\n")
                    helper.addDaily(s)
                elif s == "x":
                    break
        
        elif s == "x":
            print("Here's how you felt while using our program:")
            print(h.ratings)
            break
        elif s == "t":
            s = input("what task would you like to add\n")
            h.head.next()
            h.head.next.addTask(s)
        elif s == "a":
            h.advance()
            s = input("How did you feel today (1-10)?\n")
            helper.ratings.append(s)