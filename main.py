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

    def setNext(self, next1):
        self.next = next1

    def getTasks(self):
        print(self.tasks)
        #for key, value in self.tasks:
        #   print(key, ":", value)

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
        if self.head.next == None:
            self.head.next = day()

    def advance(self):
        self.next()
        head = head.next

    @staticmethod
    def addDaily(task):
        helper.daily[task] = "incomplete"

    @staticmethod
    def removeDaily(task):
        del helper.daily[task]


def mainLoop():
    h = helper()
    while True:
        s = input("d to get info on today, c to complete tasks, t to get add tasks to tomorrow, a to advance to tomorrow, x to exit\n")
        if s == "c":
            s = input("what task would you like to update\n")
            h.head.completeTask(s)
        elif s == "d":
            h.head.getTasks()
        elif s == "x":

            break
        elif s == "t":
            s = input("what task would you like to add\n")
            h.head.next()
            h.head.next.addTask(s)
        elif s == "a":
            h.advance()
            s = input("How did you feel today (1-10)?\n")
            helper.ratings.append(s)