"""
Command Line To-Do App

Features:
- Add Task: Allows the user to add a new task to the to-do list.
- View Tasks: Displays the current list of tasks.
- Delete Tasks: Enables the user to remove completed tasks.
- Quit: Exits the To-Do App.

Usage:
- Follow the on-screen prompts to navigate through the menu options.
- Enter 'q' or 'quit' to exit the application.

Enjoy staying organized with your to-do list!
"""


#To Clear the before every run.
import os
os.system('cls' if os.name == 'nt' else 'clear')

tasks = [
    "Morning jog",
    "Water plants",
    "Read chapter",
    "Healthy snack",
    "Email replies",
    "Quick stretch",
    "Gratitude list",
    "Short walk",
    "Review tasks",
    "Positive message"
]

def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome():
    print(
"""Welcome To the To-Do App:
1.Add New Tasks
2.View Existing Tasks
3.Delete Tasks
4.Quit
Choose Any Corresponding Number From The Above Options."""
    )

def userinput():
    while True:
        try:
            user_input = int(input("Enter Your Choice:"))
            clrscr()
            if user_input == 1:
                addtasks()
            elif user_input == 2:
                viewtasks()
            elif user_input == 3:
                deletetasks()
            elif user_input == 4:
                quit()
            else:
                print("Enter Correct Input Between 1-4:")
                welcome()
                userinput()
            break
        except ValueError:
            clrscr()
            print("Invalid Input: Enter Number Only!")
            welcome()

def addtasks():
    newtask = str(input("Enter Your Task:"))
    clrscr()
    if newtask == "" or newtask.isspace():
        print("Cannot Add Blank Tasks!")
        addtasks()
    else:
        tasks.append(newtask)
        print(f"{newtask} is Added To The Tasks List")
        while True:
            addmoretasks = str(input("Do you want to add more tasks(Y/N)"))
            clrscr()
            if addmoretasks.lower() == "y":
                addtasks()
                break
            elif addmoretasks.lower() == "n":
                clrscr()
                welcome()
                userinput()
                break
            else:
                print("Invalid Input! Try Again.")

def main_menu():
    while True:
        mainmenu = str(input("Do You Want To go to Main Menu(Y/N):"))
        clrscr()
        if mainmenu.lower() == "y":
            clrscr()
            welcome()
            userinput()
            break
        elif mainmenu.lower() == "n":
            clrscr()
            print("Thanks for using To-Do App.")
            break
        else:
            print("Invalid Input! Try Again.")

def viewtasks():
    while True:
        if len(tasks) == 0:
            clrscr()
            print("There are No tasks To-Do.")
            main_menu()
            break
        else:
            print("These Are The Tasks In The To-Do List:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            main_menu()
            break

def deletetasks():
    if len(tasks) == 0:
        clrscr()
        print("There are No tasks To-Do.")
        main_menu()
    else:
        while True:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            try:
                delete_task = int(input("Enter the No. of the Task To Delete:"))
                clrscr()
                break
            except ValueError:
                clrscr()
                print("Invalid Input: Enter Number Only!")
        if delete_task in range(1, len(tasks)+1):
            tasks.pop(delete_task-1)    
            print(f" Task {delete_task} is Deleted from The Tasks List")
        else:
            print(f"There is No Task With that Number {delete_task}. Try Again")
            deletetasks()
        while True:
            deletemoretasks = str(input("Do you want to Delete more tasks(Y/N)"))
            clrscr()
            if deletemoretasks.lower() == "y":
                deletetasks()
                break
            elif deletemoretasks.lower() == "n":
                clrscr()
                welcome()
                userinput()
                break
            else:
                clrscr()
                print(f"Invalid Input. Try Again")

def quit():
    while True:
        isquit = str(input("Do You Want To Quit(Y/N):"))
        clrscr()
        if isquit.lower() == "y":
            print("Thanks for using To-Do App.")
            break
        elif isquit.lower() == "n":
            welcome()
            userinput()
            break
        else:
            print("Invalid Input! Try Again.")

def runapp():
    welcome()
    userinput()
    
runapp()