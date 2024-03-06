import json
#                                 REGISTER FUNCTION
def register():
    firstName = input('enter your first name: ')
    lastName = input('enter your last name: ')
    email = input('enter your email: ')
    password = input('enter your password: ')
    confirmPassword = input('confirm your password: ')
    
    if confirmPassword != password:
        print('confirm your password correctly')
        return
    
    phone = input('enter your phone: ')
    userInfo = {'firstName': firstName, 'lastName': lastName, 'email': email, 'password': password, 'phone': phone}

    # Read existing data or initialize an empty list
    try:
        with open("task.json", 'r') as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = []
    except FileNotFoundError:
        data = []

    # Append new user info
    data.append(userInfo)

    # Write back to the file
    with open("task.json", 'w') as f:
        json.dump(data, f, indent=4)


#                                     ADD PROJECT
def addproject(x):
    title = input('enter your project title: ')
    details = input('enter your project details: ')
    totalTarget = input('enter your total target: ')
    startTime = input('enter your start time: ')
    projectInfo = {'email': x, 'title': title, 'details': details, 'totalTarget': totalTarget, 'startTime':startTime}
    try:
        with open("project.json", 'r') as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = []
    except FileNotFoundError:
        data = []
    # Append new prject info
    data.append(projectInfo)

    # Write back to the file
    with open("project.json", 'w') as f:
        json.dump(data, f, indent=4)

#                                    VIEW PROJECTS
def viewProjects():
        f1 = open("project.json",'r')
        for line in f1:
           print(line)

#                                    UPDATE PROJECT
def updateproject(x):
    title = input('Enter the project title you want to update: ')
    with open("project.json", 'r') as f:
        data = json.load(f)

    for task in data:
        if task['title'] == title and task['email'] == x:
            print('---------------------------EDIT MENU----------------------------------------')
            print('1 => Change title    2 => Change details\n3 => Change totalTarget    4 => Change startTime: ')
            print('----------------------------------------------------------------------------')
            choice = input('enter your choice : ')
            if choice == '1':
                updateTitle = input('Enter the new title: ')
                task['title'] = updateTitle
            elif choice == '2':
                updateDetails = input('Enter the new details: ')
                task['details'] = updateDetails
            elif choice == '3':
                updateTotalTarget = input('Enter the new total target: ')
                task['totalTarget'] = updateTotalTarget
            elif choice == '4':
                updateStartTime = input('Enter the new start time: ')
                task['startTime'] = updateStartTime
            else:
                print('Invalid option')
                break
    
    # Write back to the file
    with open("project.json", 'w') as f:
        json.dump(data, f, indent=4)
            

#                                    DELETE PROJECT
def deleteProject(x):
    title = input('Enter the project title you want to delete: ')
    with open("project.json", 'r') as f:
        data = json.load(f)

    # Create a new list to store projects without the one to be deleted
    new_data = [task for task in data if not (task['title'] == title and task['email'] == x)]

    # Check if any project was deleted
    if len(new_data) == len(data):
        print("Project not found or you don't have permission to delete it.")
    else:
        with open("project.json", 'w') as f:
            json.dump(new_data, f, indent=4)
            print("Project successfully deleted.")
 


#                                    LOGIN FUNCTION
def login():
    email = input('enter your email: ')
    password = input('enter your password: ')
    f1 = open("task.json",'r')
    data = json.load(f1)
    for user in data:
       if user['email'] == email and user['password'] == password:
                print('Login successful!')
                while True:
                    print('-----------------------------PROJECT MENU-----------------------------------')
                    print('1 => add new project   2 => view all projects\n3=>update project       4=>delete project    5=>log out')
                    print('----------------------------------------------------------------------------')
                    choice = input('enter your choice: ')
                    if choice == '1':
                        addproject(email)
                    elif choice == '2':
                        viewProjects()
                    elif choice == '3':
                        updateproject(email)
                    elif choice == '4':
                        deleteProject(email)
                    elif choice == '5':
                        print('Logging out...')
                        break
                    else:
                        print('Invalid choice. Please try again.')
                        return
    print('Invalid email or password..')






print('enter your choice: ')
print('1 => Register   2 => Log in')
choice = input('enter your choice: ')

if choice == '1':
    register()
elif choice == '2':
    login()
else:
    print('3')
