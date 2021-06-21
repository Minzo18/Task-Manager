#Import the datetime library
from datetime import datetime


###################################################################################################
#NEW USER REGISTRATION FUNCTION

#Define a user registration function
def reg_user(username, reg_usernames, database):
    
    #The instructions to add a new user are displayed
    if username == 'admin':
        print("\nREGISTER A NEW USER\n\nEnter the username and password for the new user.\nEnter the password twice to confirm that it is correct.\n")

        #Declare a boolean set to True to check when an existing username is entered. When the username entered is not an existing one, the boolean will change to False.
        duplicate = True

        #This while loop will keep asking for a username until the admin enters a username that is not existing
        while duplicate == True:

            #Request the username of the new user
            new_user = input("Username: ")

            #The If statement will check if the new username exists in the list of registered usernames. If it does, it prints out the message to enter a different username.
            if new_user in reg_usernames:
                print("This username already exists. Please enter a different username.")

            #If the username does not exist, it will change the boolean to False to exit the while loop
            else:
                duplicate = False

        #Declare a boolean set to False to check when the correct password is entered twice. When the passwords match, the boolean will change to True.
        pw_match = False

        #The while loop will keep repeating until the boolean changes to True.
        while pw_match == False:
            
            #Request the password twice
            new_user_pw = input("Password: ")
            new_pw_confirm = input("Confirm password: ")

            #If the two passwords are the same, the username and password will be added to the database and the pw_match boolean is set to True. The while loop will be exited.
            if new_user_pw == new_pw_confirm:
                database.write(new_user + ", " + new_user_pw + "\n")
                print("\nNew user added successfully.")
                pw_match = True
                
            #If the passwords do not match, the user will be prompted to enter the passwords again.
            else:
                print("\nPasswords do not match. Enter it again.")

    else:
        print("\nYou do not have administrator rights to add a new user.")


###################################################################################################
#ADD A TASK FUNCTION

#Define an add task function
def add_task(reg_usernames, tasks_file):

        #Request username of person that task will be assigned to
        print(f"\nADD A NEW TASK\n\nEnter the username of the employee that the task will be assigned to. The username entered should be a valid username from the following list of registered users:\n")

        #Display list of registered users
        for i in range(0,len(reg_usernames)):
            print(reg_usernames[i])

        #Check that the username entered is valid
        #Declare username_check boolean to False. When a valid username is entered, the boolean will change to True.
        #The while loop will keep repeating until the boolean changes to True. 
        username_check = False
        while username_check == False:

            #Request username for the new task
            nt_username = input("\nUsername: ")
            
            #The for loop will check the username entered and compare it to each item in the list reg_usernames. When it finds a match, it will change the boolean to True to exit the while loop.
            for i in range(0, len(reg_usernames)):
                if reg_usernames[i] == nt_username:
                    username_check = True

            #If the for loop reaches the end of its range and the username entered does not match any of the registered usernames, the boolean stays False.
            #Display the result and request the user to enter a valid username.
            if username_check == False:
                print("\nUsername does not appear in the list above. Please enter a valid username.\n")

        #Once a valid username has been entered, request the tast title, description and due date
        print("\nEnter the title, description and due date of the task. The due date should be added in the format DD Mmm YYYY.\n")

        nt_title = input("Title: ")
        nt_description = input("Description: ")
        nt_due_date = input("Due date (e.g. 01 Jan 2021): ")

        #The date assigned is the current date. Using the datetime library, the current date will be stored to the variable now.
        now = datetime.now()
        #To get the date in the required format, use the strftime function and the relevant directive
        #%d = date of the month
        #%b = abbreviation of the month in words
        #%Y = current year including century
        nt_date_assigned = now.strftime('%d') + " " + now.strftime('%b') + " " + now.strftime('%Y')

        #As a default, all new tasks are not completed
        nt_completed = 'No'

        #The new task is written to the tasks file in the format username, title, description, date assigned, due date, completed
        tasks_file.write(nt_username + ", " + nt_title + ", " + nt_description + ", " + nt_date_assigned + ", " + nt_due_date + ", " + nt_completed + "\n")

        #Display message to say task added successfully
        print("\nNew task added successfully.")


###################################################################################################
#VIEW ALL TASKS FUNCTION

#Define a function to view all tasks
def view_all(usernames, title, description, date_assigned, due_date, completed):
    
    #Display all the tasks saved in the tasks.txt file
    print("\nVIEW ALL TASKS\n")
    print("--------------------------------------------------------------------------------")

    #The for loop will repeat for the number of tasks in the list usernames which equates to the number of tasks saved in the tasks file
    for i in range(0,len(usernames)):

        #Each section of data for each task will be displayed
        print("TASK NUMBER " + str(i+1) + "\t\t\t\t\tTASK ASSIGNED TO: " + usernames[i] + "\n")
        print("TITLE: " + title[i] + "\n")
        print("TASK DESCRIPTION:\n" + description[i] + "\n")
        print("DATE ASSIGNED:" + date_assigned[i] + "\t|DUE DATE:" + due_date[i] + "\t\t|COMPLETED:" + completed[i] + "\n")
        print("--------------------------------------------------------------------------------")


###################################################################################################
#VIEW MY TASKS FUNCTION

#Define a function to view all functions
def view_mine(username, usernames, title, description, date_assigned, due_date, completed):

    #Display all the tasks saved in the tasks.txt file that are assigned to the user currently logged in.
    print("\nVIEW MY TASKS\n")
    print("--------------------------------------------------------------------------------")

    #Declare variable t used to count the number of tasks assigned to the user logged in.
    t = 1

    #Define a dictionary to correlate task numbers per user to the task numbers as they appear in the tasks.txt file
    tasks = {}

    #The for loop will repeat for the number of tasks in the list usernames which equates to the number of tasks saved in the tasks file
    for i in range(0,len(usernames)):

        if usernames[i] == username:
                
            #Each section of data for each task will be displayed
            print("TASK NUMBER " + str(t) + "\t\t\t\t\tTASK ASSIGNED TO: " + usernames[i] + "\n")
            print("TITLE: " + title[i] + "\n")
            print("TASK DESCRIPTION:\n" + description[i] + "\n")
            print("DATE ASSIGNED:" + date_assigned[i] + "\t|DUE DATE:" + due_date[i] + "\t\t|COMPLETED:" + completed[i] + "\n")
            print("--------------------------------------------------------------------------------")

            #Store the task number for the user as a key and the task number in the tasks file as a value in the dictionary
            tasks[t] = i
            
            #Increment t when a task under the username logged in is displayed.
            t += 1

    #If t stays at 1 then it means no tasks were displayed for the user. Therefore there are no tasks assigned to the user.
    if t == 1:
        print("No tasks currently assigned to you.")

    else:
        #print(tasks)      

        #Define boolean set to False. When a valid input is received, boolean changes to True to exit while loop
        input_check = False
        while input_check == False:

            #Ask user to enter which task to edit
            task_num = input("\nTo edit a task or mark it as completed, enter the task number.\n\nTo return to the main menu, enter -1.\n")

            #Check if the input character is a number
            if task_num.isdigit() == True:
                                           
                #Check that the number entered appears in the dictionary tasks, if it does then the input is valid.
                if int(task_num) in tasks:

                    input_check = True

                    #x is the number at which the task appears in the tasks.txt file and in the lists where the tasks data is stored.
                    x = tasks[int(task_num)]

                    #Check that the task is not completed before editing it
                    if completed[x] == 'No':

                        #Ask user to choose how they want to edit the task
                        et_option = input('''\nSelect an option below to edit the task:
                        m - mark the task as completed
                        u - assign the task to a different user
                        d - change the due date of the task\n''')

                        if et_option == 'm':

                            #To mark the task as complete, the data stored in the list 'completed' and indexed to position 'x' must be changed to Yes
                            completed[x] = 'Yes'
                            print("Task number " + task_num + " titled as " + title[x] + " has been marked as completed.\n")

                        elif et_option == 'u':

                            #To change the username, use the code from the function assign new task to select a new user
                            print("Please enter a username from the list below.")
                                
                            #Display list of registered users
                            for i in range(0,len(reg_usernames)):
                                print(reg_usernames[i])

                            #Check that the username entered is valid
                            #Declare username_check boolean to False. When a valid username is entered, the boolean will change to True.
                            #The while loop will keep repeating until the boolean changes to True. 
                            username_check = False
                            while username_check == False:

                                #Request the new username for the task
                                username_edit = input("\nUsername: ")
                                    
                                #The for loop will check the username entered and compare it to each item in the list reg_usernames. When it finds a match, it will change the boolean to True to exit the while loop.
                                for i in range(0, len(reg_usernames)):
                                    if reg_usernames[i] == username_edit:
                                        username_check = True
                                        usernames[x] = username_edit

                                #If the for loop reaches the end of its range and the username entered does not match any of the registered usernames, the boolean stays False.
                                #Display the result and request the user to enter a valid username.
                                if username_check == False:
                                    print("\nUsername does not appear in the list above. Please enter a valid username.\n")
                                            

                        elif et_option == 'd':

                            #To change the due date, the data stored in the list 'due_date' and indexed to position 'x' must be changed to the new date
                            due_date[x] = input("Enter the new due date (e.g. 01 Jan 2021): ")

                        #Overwrite the text file with all the tasks to store the new information
                        with open('tasks.txt', 'r+') as tasks_file:
                            for i in range(0,len(usernames)):
                                tasks_file.write(usernames[i] + ", " + title[i] + ", " + description[i] + ", " + date_assigned[i] + ", " + due_date[i] + ", " + completed[i] + "\n")

                    #If the task is already marked as completed, it cannot be edited
                    else:
                        print("\nThis task has already been completed and cannot be edited.")
                            
                #If the user enters -1, return to the main menu
                elif int(task_num) == -1:
                    return()

                #If the user enters a value that does not exist in the tasks dictionary, an error message is displayed.
                else:
                    print("Task number does not exist.\n")

            #If the user enters an unknown character that does not exist in the tasks dictionary, an error message is displayed.
            else:
                print("Invalid entry.\n")
                  
       
###################################################################################################
#GENERATE REPORTS FUNCTION

#Define a function to generate reports
def gen_reports(usernames, completed, due_date, reg_usernames):

#TASK OVERVIEW REPORT

    #Number of tasks is equal to the number of items in the list usernames
    nr_tasks = len(usernames)

    #Declare counters
    nr_tasks_completed = 0
    nr_tasks_uncompleted = 0
    nr_tasks_overdue = 0

    #The current date will be stored to the variable now. Date required to see if tasks are overdue.
    now = datetime.now().date()
    #print(now)

    #Use for loop to run through all the tasks and use if and elif statements to check which are completed
    for i in range(0, len(usernames)):
        if completed[i] == 'Yes':
            nr_tasks_completed += 1

        elif completed[i] == 'No':
            nr_tasks_uncompleted += 1

            #If a task is incomplete, use if statement to check if the due date has passed
            #To get the due date in the required format so that it can be compared to today's date, use the strptime function and the relevant directive
            #%d = date of the month
            #%b = abbreviation of the month in words
            #%Y = current year including century
            duedate_format = datetime.strptime(due_date[i], "%d %b %Y").date()
            #print(duedate_format)

            if duedate_format < now:
                nr_tasks_overdue +=1

    #Calculate the percentage of tasks incomplete
    perc_uncompleted = round(((nr_tasks_uncompleted / nr_tasks) * 100), 2)

    #Calculate the percentage of tasks overdue
    perc_overdue = round(((nr_tasks_overdue / nr_tasks) * 100), 2)

    #print(f'''\nTASK OVERVIEW REPORT\n
#Total number of tasks:\t\t\t{nr_tasks}
#Total number of tasks completed:\t{nr_tasks_completed}
#Total number of tasks incomplete:\t{nr_tasks_uncompleted}
#Total number of tasks overdue:\t\t{nr_tasks_overdue}
#Percentage of tasks incomplete:\t\t{perc_uncompleted}%
#Percentage of tasks overdue:\t\t{perc_overdue}%''')

    #Open the task overview file in write mode and write the information to it
    with open('task_overview.txt', 'w') as tasks_report:
        tasks_report.write(f'''\nTASK OVERVIEW REPORT\n
Total number of tasks:\t\t\t{nr_tasks}
Total number of tasks completed:\t{nr_tasks_completed}
Total number of tasks incomplete:\t{nr_tasks_uncompleted}
Total number of tasks overdue:\t\t{nr_tasks_overdue}
Percentage of tasks incomplete:\t\t{perc_uncompleted}%
Percentage of tasks overdue:\t\t{perc_overdue}%\n''')



#USER OVERVIEW REPORT

    #Open the user overview file in write mode
    users_report = open('user_overview.txt', 'w')

    #Total number of users is the number of items in the list reg_usernames
    nr_users = len(reg_usernames)

    #print(f'''\nUSER OVERVIEW REPORT\n
#Total number of users registered:\t{nr_users}
#Total number of tasks:\t\t\t{nr_tasks}
#''')

    users_report.write(f'''\nUSER OVERVIEW REPORT\n
Total number of users registered:\t{nr_users}
Total number of tasks:\t\t\t{nr_tasks}
''')

    #Use for loop to go through each username in the reg_usernames list to find projects assigned to the specific user
    for i in range(0, len(reg_usernames)):

        #Declare counters
        task_count = 0
        nr_completed = 0
        nr_uncompleted = 0
        nr_overdue = 0

        #print(f"\nUSERNAME: {reg_usernames[i]}\n")

        #Display which users information will be displayed
        users_report.write(f"\nUSERNAME: {reg_usernames[i]}")

        #Use nested for loop to check usernames in the tasks 
        for j in range(0, len(usernames)):

            #The if statement will find the tasks assigned to the specific user and count them
            if reg_usernames[i] == usernames[j]:
                task_count += 1

                #Use if and elif statements to check how many tasks for the user are completed or incompleted
                if completed[j] == 'Yes':
                    nr_completed += 1

                elif completed[j] == 'No':
                    nr_uncompleted += 1

                    #If a task is incomplete, use if statement to check if the due date has passed
                    #To get the due date in the required format, use the strptime function and the relevant directive
                    #%d = date of the month
                    #%b = abbreviation of the month in words
                    #%Y = current year including century
                    duedate_format = datetime.strptime(due_date[j], "%d %b %Y").date()
                    #print(duedate_format)
                    
                    if duedate_format < now:
                        nr_overdue +=1
                    

        #If the user has no tasks assigned to them, display a message
        if task_count == 0:
            #print(f"\nNo tasks assigned to {reg_usernames[i]}.\n")
            users_report.write(f"\nNo tasks assigned to {reg_usernames[i]}.\n")

        #Else calculate the various percentages
        else:
            perc_tasks_assigned = round(((task_count / nr_tasks) * 100), 2)
            perc_tasks_completed = round(((nr_completed/task_count)* 100), 2)
            perc_tasks_uncompleted = round(((nr_uncompleted/task_count)* 100), 2)
            perc_tasks_overdue = round(((nr_overdue/task_count)* 100), 2)
            
            #print(f'''\nTotal tasks assigned:\t\t\t{task_count}
#Percentage of tasks assigned:\t\t{perc_tasks_assigned}%
#Percentage of tasks completed:\t\t{perc_tasks_completed}%
#Percentage of tasks incomplete:\t\t{perc_tasks_uncompleted}%
#Percentage of tasks overdue:\t\t{perc_tasks_overdue}%\n''')

            #Write the information to the file for the specific user
            users_report.write(f'''\nTotal tasks assigned:\t\t\t{task_count}
Percentage of tasks assigned:\t\t{perc_tasks_assigned}%
Percentage of tasks completed:\t\t{perc_tasks_completed}%
Percentage of tasks incomplete:\t\t{perc_tasks_uncompleted}%
Percentage of tasks overdue:\t\t{perc_tasks_overdue}%\n''')


    #Close the file
    users_report.close()


###################################################################################################
#LOOPING STRUCTURE

#Declare a login boolean to False. When the boolean changes to True, the user will be logged in.
login = False

#This is a looping structure that will keep the program running till the user chooses the exit option.
while 1:


###################################################################################################
#USER FILE READ

    #Declare empty lists that will be used to store the usernames and passwords saved on the text file user.txt
    reg_usernames = []
    reg_passwords = []

    #Open the file user.txt and store it under database
    database = open('user.txt','r+')
    for line in database:                               #For loop to read each line in the file
        users = line.split(', ')                        #Split the user name with delimiter ', 'and save it to the list users
        #print(users)                                   #For error checking remove the hash # to see the list of users and passwords stored in user.txt
        reg_usernames.append(users[0])                  #Item one in the list will be the username. Append it to the list called reg_usernames
        reg_passwords.append(users[1].strip('\n'))      #Item two in the list will be the password. Append it to the list called reg_passwords. The new line at the end of each password must also be removed.

    #print(reg_usernames)                               #For error checking remove the hash # to see the list of users and passwords stored in the lists reg_usernames and reg_passwords
    #print(reg_passwords)


###################################################################################################
#TASKS FILE READ

    #Declare empty lists to store each type of data
    usernames = []
    title = []
    description = []
    date_assigned = []
    due_date = []
    completed = []

    #Open the file tasks.txt and store it as tasks_file
    tasks_file = open('tasks.txt', 'r+')
    for line in tasks_file:                             #For loop to read each line in the file
        data = line.split(', ')                         #Split the data with delimiter ', 'and save it to the list data
        #print("Data = " + str(data) + "\n")            #For error checking remove the hash # to see the data being read from the file tasks.txt
        usernames.append(data[0])                       #Each section of data is appended to the relevant type of list 
        title.append(data[1])
        description.append(data[2])
        date_assigned.append(data[3])
        due_date.append(data[4])
        completed.append(data[5].strip('\n'))

    #print(usernames)                                   #For error checking remove the hash # to see the data has been read correctly from the tasks.txt file
    #print(title)
    #print(description)
    #print(date_assigned)
    #print(due_date)
    #print(completed)


###################################################################################################
#LOGIN



    #Start a while loop that will keep repeating until login changes to True.
    while login == False:

        #Declare index variable. When the username is found in the reg_username list. 
        username_index = -1                                     
        
        #Declare booleans for the username and password set to False. When the correct username and password is found in the lists, the booleans will change to True.
        username_check = False
        password_check = False
    
        #Display a welcome message
        #Request the user to input their username and password
        print("\n********************************************************************************")
        print("\nWELCOME TO THE TASK MANAGER")
        print("\nPlease enter your username and password to login.\n")
        username = input("Username: ")
        password = input("Password: ")

        #The for loop will repeat for amount of usernames found in reg_username
        #Each iteration will compare the entered username to the ones in the list using the IF statement
        #If the correct username is found the index will be stored and the username check boolean will change to True
        for i in range(0, len(reg_usernames)):
            if reg_usernames[i] == username:
                username_index = i
                username_check = True

        #The index of the username is used to check if the correct password is entered and the password check boolean changes to True if it is correct
        if reg_passwords[username_index] == password:
            password_check = True

        #Login Test
        #The username_check and password_check booleans must be True 
        #There are 3 possible outcomes, therefore 3 IF statements

        #1. Username and password is True and indices equal. The login boolean changes to True and while loop is exited. The user will be logged in.
        if username_check == True and password_check == True:
            login = True
            print("\nUsername and password correct. Login successful.")

        #2. Username False. Display the relevant message and the while loop restarts prompting user to enter a username and password.
        if username_check == False:
            print("\nIncorrect username entered. Enter a valid username and password.")

        #3. Username True and password False. Display the relevant message and the while loop restarts prompting user to enter a username and password.
        if username_check == True and password_check == False:
            print("\nIncorrect password entered. Enter a valid username and password.")
             


###################################################################################################
#USER MENU        

    if username == 'admin':
        
        option = input('''\n********************************************************************************
    \nUSER MENU
    \nPlease select one of the following options:\n
    r - register user
    a - add task
    va - view all tasks
    vm - view my tasks
    gr - generate reports
    s - statistics
    l - logout
    e - exit\n\n''')

        print("\n********************************************************************************")

    else:
        option = input('''\n********************************************************************************
    \nUSER MENU
    \nPlease select one of the following options:\n
    r - register user
    a - add task
    va - view all tasks
    vm - view my tasks
    gr - generate reports
    l - logout
    e - exit\n\n''')

        print("\n********************************************************************************")


###################################################################################################
#NEW USER REGISTRATION

    #If the user selects r, it calls the reg_user function
    if option == 'r':
        reg_user(username, reg_usernames, database)


###################################################################################################
#ADD A TASK

    #If the user selects a, it calls the add_task function
    if option == 'a':
        add_task(reg_usernames, tasks_file)


###################################################################################################
#VIEW ALL TASKS

    #If the user selects va, it calls the view_all function
    if option == 'va':
        view_all(usernames, title, description, date_assigned, due_date, completed)
        

###################################################################################################
#VIEW MY TASKS

    #If the user selects vm, it calls the view_mine function
    if option == 'vm':
        view_mine(username, usernames, title, description, date_assigned, due_date, completed)


###################################################################################################
#GENERATE REPORTS

    if option == 'gr':
        gen_reports(usernames, completed, due_date, reg_usernames)
        
###################################################################################################
#STATISTICS

    #If the admin selects s, display all the total number of tasks and the total number of users.
    if option == 's':
        print("\nSTATISTICS\n")

        gen_reports(usernames, completed, due_date, reg_usernames)

        with open('task_overview.txt', 'r') as tasks_report:
            for line in tasks_report:
                print(line)

        with open('user_overview.txt', 'r') as users_report:
            for line in users_report:
                print(line)

        #Display the total number of tasks by displaying the number of items in the list usernames.
        #print("\nTotal number of tasks assigned:\t\t" + str(len(usernames)))

        #Display the total number of users by displaying the number of items in the list reg_usernames.
        #print("\nTotal number of users registered:\t" + str(len(reg_usernames)))

        #Display the number of tasks assigned to each user.
        #print("\nTotal number of tasks assigned to each user:\n")
        #for i in range(0, len(reg_usernames)):
            #task_count = 0
            #for j in range(0, len(usernames)):
                #if reg_usernames[i] == usernames[j]:
                    #task_count += 1

            #print(f"{reg_usernames[i]} = {task_count}")
                

###################################################################################################
#LOGOUT

    #If the user selects l, the user is logged out but the program does not close.
    if option == 'l':            
            login = False


###################################################################################################
#EXIT

    #If the user selects e, the program exits.
    if option == 'e':            
            exit()

    
###################################################################################################
#CLOSE THE FILES
            
database.close()    
tasks_file.close()
