# ===== Importing external modules ===========
from datetime import date

# The given file "user.txt" doesn't contain a newline character 
# after the first entry. It is recommended that the user add one 
# before running this program

# ==== Login Section ====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and passwords from the user.txt file
    - You can use a list or dictionary to store a list of usernames and
       passwords from the file.
    - Use a while loop to validate your user name and password.
'''
def login():
    """Authenticate user and return username if successful."""
    username = input("Username: ")
    password = input("Password: ")

    with open("user.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(", ")

            if username == stored_username and password == stored_password:
                print("Login successful")
                return username

    print("Invalid credentials")
    return None


with open("user.txt", "r") as file:
    users = {}

    for line in file:
        username, password = line.strip().split(", ")
        users[username] = password

# Get user to login
current_user = login()

while True:
    # Present the menu to the user and
    # make sure that the user input is converted to lower case.
    menu = input(
        '''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: '''
    ).lower()

    if menu == 'r':
        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")
        confirm_password = input("Confirm your password: ")
        # Check if the new password and confirmed password are the same
        # then add them to the user.txt file, otherwise present a relevant message
        if password == confirm_password:
            with open("user.txt", "a") as file:
                file.write(f"{username}, {password}\n")
            print("User registered successfully.")
        else:
            print("Passwords do not match. Please try again.")

    elif menu == 'a':
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not
              complete.
        '''
        # Prompt a user for the desired information
        username = input("Enter the username of the person to whom the task is assigned: ")
        title = input("Enter the title of the task: ")
        description = input("Enter the description of the task: ") 
        try:
            due_date = input("Enter the due date of the task DD-MM-YYYY: ")
            # Validate the due date format
            date.strptime(due_date, "%d-%m-%Y")
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")
            continue

        # Get the current date and format it e.g. 1 Jan 2024
        current_date = date.today().strftime("%-d-%b-%Y")
        # Add the data to the file task.txt
        with open("tasks.txt", "a") as file:
            file.write(f"{username}, {title}, {description}, {due_date}, {current_date}, No\n")
        print("Task added successfully.")


    elif menu == 'va':
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in
              the PDF
            - It is much easier to read a file using a for loop.'''
        with open("tasks.txt", "r") as file:
            for line in file:
                if not line.strip():
                    continue  # skip empty lines

                user_name, title, description, due_date, current_date, no = [
                    x.strip() for x in line.split(",")
                ]

                print(f"""
            ------------------------------------------------------
            Task:                                 {title}
            Assigned to:                          {user_name}
            Date assigned:                        {current_date}
            Due date:                             {due_date}
            Task Complete?                        {no}
            Task description:                     {description}
            ------------------------------------------------------
            """)
    elif menu == 'vm':
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''
        with open("tasks.txt", "r") as file:
            for line in file:
                # Skip empty lines
                if not line.strip():
                    continue

                # Split and clean the data
                parts = [p.strip() for p in line.strip().split(",")]

                # Validate structure
                if len(parts) != 6:
                    print("Skipping malformed line:", line)
                    continue

                file_username, title, description, due_date, current_date, no = parts

                # Check if task belongs to logged-in user
                if file_username == current_user:
                    print(f"""
                            Task:               {title}
                            Assigned to:        {file_username}
                            Date assigned:      {current_date}
                            Due date:           {due_date}
                            Task description:   {description}
                            """)

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")