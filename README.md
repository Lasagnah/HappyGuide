# Happy Guide
## Introduction
The goal of this project is to create an application/program which will help the user maximize happiness. The way which we will do this is through creating daily tasks for the user to complete, with the end goal of each to make the user more happy. 
This project helps to maximize happiness through creating a system which can easily allow for the user to define daily tasks and create a checklist of tasks for them to complete, as setting goals and achieving them has been seen to make people more happy in the past.
## Installation
As for installing our program, all that is needed is to use the main.py file and run the mainLoop function. That will put the user in a loop with command line prompts as to what they want to do. As for instructions on how to use, you can follow the instructions on the command line.
## Functionalities
### Overview
We created a linked list class, where when we attempt to use the node after the last, we simply generate a new node.
### Day Class
The day class acts as our Node class. We number each day, with an increasing class variable. Whenever we generate a new day, we copy the daily tasks over from the helper class as a basis for the new list of tasks. 
As for local variables, we have day number, next day, and a dictionary which consists of pairs in the format task : completion. 
As for methods for this class, we include:
* Initialization, which involves copying information from the daily tasks to our local variable, identifying a day's number, and iddentifying the next day.
* Updating tasks, which involves the UpdateTask and CompleteTask methods. We simply change the value of the key value pair to the given parameter. 
* Updating fields, which involves changing the object's next field. 
* Adding, which involves the AddTask and UpdateTask methods. We add a task to the list of tasks. UpdateTask is included here because if a task is not found in the list of tasks, it is created. 
* Retrieving, which involves the getTasks method. It simply prints all tasks and their completion.
### Helper Class
We include two class variables, the daily list, and the ratings list. The daily list is used as a list of daily tasks that will be copied over from day to day. The ratings list is used as a way of measuring how happy a user is. When the user advances forward a day, they are asked to rate their day, and their rating is added to the ratings list. For methods, we have
* Initialization, which adds a day to the head of the list, and adds a task to the first day, to configure their HappyGuide.
* 3 static methods, which all surround the daily list. We have adding a daily task, removing a daily task, and getting the daily tasks.
* Next is a method which checks to see if the next day exists. If it exists, it does nothing. If it doesn't exist, then we create a new day and make it pointed to by the head's next field.
* Advance is a method which first calls Next, then changes the head field to be the head's next field. 
### MainLoop
First we initialize a helper object, then we enter a loop. 
We take input from the user, then depending upon the user's input we do one of a few possible things including:
* Update today's tasks, which calls the UpdateTask method after asking for the user to specify a task and if completed.
* Print today's tasks, which just calls the getTasks method.
* Exit the program, which prints the ratings field of the helper object, before breaking out of the loop. 
* Add a task to tomorrow, which calls Next to guarantee that there is an object tomorrow, then calls the addTask method to add a task to the next day.
* Advance a day, which calls the advance method, followed by asking the user how they felt, and appending that to the helper's ratings list.
* Editing the daily tasks, which enters another loop. This loop takes input from the user, and then will either add a task, print daily tasks, or remove a task from the list of daily tasks. It also requires the user to give a specific input to break out of this interior loop. 
## Test Cases
As for the test cases in testcases.py, they will do the following:
* TestCase1 will test initializing a helper object, and will test printing the tasks of the helper object.
TestCase 1 will return \
configure HappyGuide : incomplete
* TestCase2 will test adding tasks to a helper object.
TestCase2 will return \
configure HappyGuide : incomplete \
test HappyGuide : completed
* TestCase3 will test the usage of daily tasks, as well as the generation and advancement to future days.
TestCase3 will return \
Get up out of bed : incomplete 
## Discussion
As for application of course materials, we clearly applied principles of object oriented programming through the creation of the day and helper classes, with their multiple different types of variables. 
One thing that we did encounter that could be improved is the specific types of variables that we used. For example, we used class level variables for our ratings and daily lists. Realistically, they didn't need to be class level variables and could instead just be variables within the mainLoop. Because they are class level variables, it isn't possible to have multiple instances running with different data for each of these variables which could potentially become a problem. There weren't many limitations encountered during the project.
## Conclusions
This program was made to maximize happiness through using a checklist system. In our linked list structure, we incorporate two classes, one which represents the list as a whole, and the other which represents the nodes. 