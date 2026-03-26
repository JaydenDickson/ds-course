"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
import email


class Email:

    has_been_read = False
    inbox = []
    def __init__(self, email_address, subject_line, email_content):
        # Initialise the instance variables for each email.
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content



# Create the 'mark_as_read()' method to change the 'has_been_read'
# instance variable for a specific object from False to True.
    def mark_as_read(self):
        self.has_been_read = True

# --- Functions --- #
# Build out the required functions for your program.


def populate_inbox():
    # Create 3 sample emails and add them to the inbox list.
    email1 = Email("user1@example.com", "Subject 1", "Content 1")
    email2 = Email("user2@example.com", "Subject 2", "Content 2")
    email3 = Email("user3@example.com", "Subject 3", "Content 3")

    email1.inbox.append(email1)
    email2.inbox.append(email2)
    email3.inbox.append(email3)


def list_emails(email):
        # Create a function that prints each email's subject line
        # alongside its corresponding index number,
        # regardless of whether the email has been read.
    for i, mail in enumerate(email.inbox), email.inbox:
        print(i, mail.subject_line)
    


def read_email(index):
    # Create a function that displays the email_address, subject_line,
    # and email_content attributes for the selected email.
    # After displaying these details, use the 'mark_as_read()' method
    # to set its 'has_been_read' instance variable to True.
    mail = Email.inbox[index]
    print(mail.email_address)
    print(mail.subject_line)
    print(mail.email_content)
    mail.mark_as_read()


def view_unread_emails():
    # Create a function that displays all unread Email object subject lines
    # along with their corresponding index numbers.
    # The list of displayed emails should update as emails are read.
    for i, mail in enumerate(Email.inbox):
        if mail.has_been_read == False:
            print(i, mail.subject_line)
            mail.mark_as_read()



# --- Lists --- #
# Initialise an empty list outside the class to store the email objects.
# --- Email Program --- #

# Call the function to populate the inbox for further use in your program.
populate_inbox()
# Fill in the logic for the various menu operations.

# Display the menu options for each iteration of the loop.
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )

    if user_choice == 1:
        # Add logic here to read an email
        index = int(input("Enter the index of the email you want to read: "))
        read_email(index)
        

    elif user_choice == 2:
        # Add logic here to view unread emails
        view_unread_emails()

    elif user_choice == 3:
        # Add logic here to quit application.
        print("Goodbye!")
        break

    else:
        print("Oops - incorrect input.")