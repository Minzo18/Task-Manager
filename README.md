# Task-Manager

This is a Task Manager program which can be used to track tasks in a company. The program requires users to login with a username and password to ensure that only registered users are accessing the information being tracked. Tasks can be added to the registry and then viewed in a user-friendly, easy to read manner. Tasks can also be edited as and when required. The program is also capable of displaying statistics and generating reports showing these statistics. 

Steps on how to use the following features are listed below:

1. Register New Users
2. Add Tasks
3. View Tasks
4. Edit Tasks or Mark it as Complete
5. Display Statistics and Generate Reports
 

## 1. Register New Users

To add a new user, follow the steps below:

1. After admin user logs in, enter "r" to select the "register user" option. 
2. Enter the username for the new user. If an existing username is entered, the program will ask the user to select a different username.
3. Enter a password for the user.
4. Enter the password again to confirm that it is correct and the new user will be added to the registry.

The new user will then be added to the user registry.

NB. Only the admin user is allowed to register new users.

## 2. Add Tasks

To add a new task, follow the steps below:

1. Enter "a" to select the "add task" option.
2. The program will display a list of all the registered users. Enter the username for the person that the task needs to be assigned to.
3. Enter the Title of the task.
4. Enter the Description of the task.
5. Enter the Due Date of the task.

The task will then be added to the task registry.

## 3. View Tasks

There are two options to view tasks. The one allows the user to view all tasks that have been logged on the system and the other option displays the tasks that are assigned to user that is currently logged in.
  
To view all the tasks, simply enter "va" to select the "view all tasks" option. To view tasks that are only assigned to the user currently logged in, enter "vm" to select the "view my tasks" option. 
When the "view my tasks" option is selected, the user is given the option to edit a task or mark it as complete. This will be covered in the next section. To return to the main menu, enter -1.

## 4. Edit Tasks or Mark it as Complete

To edit a task or mark it as complete, follow the steps below.

1. Enter "vm" option to select the "view my tasks" option.
2. For the task that needs to be editted, enter the task number as it appears in the list.
3. The user will be presented with 3 options shown below:

          m - mark the task as completed
          u - assign the task to a different user
          d - change the due date of the task

4. If the user enters "m", the task will be marked as complete and return to the main menu.
5. If the user enters "u", the program will display a list of all registered usernames and ask the user to enter the username for the person that the task should be assigned to and then return to the main menu.
6. If the user enters "d", the program will ask the user to enter the new due date for the task and then return to the main menu.

## 5. Display Statistics and Generate Reports

The program will generate two reports when the "generate reports" option is selected. The one report is a task overview report and the other is a user overview report. 

The task overview report includes the following information:

* Total number of tasks
* Total number of tasks completed
* Total number of tasks incomplete
* Total number of tasks overdue
* Percentage of tasks incomplete
* Percentage of tasks overdue

The user overview report includes the following information:

* Total number of users
* Total number of tasks

In addition, the report also includes the following information for each user:

* Total tasks assigned
* Percentage of tasks assigned
* Percentage of tasks completed
* Percentage of tasks incomplete
* Percentage of tasks overdue

The reports are stored as .txt files in the directory where the program is stored.






