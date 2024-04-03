#  The login project

import os
from tkinter import *
import mysql.connector
from tkinter import messagebox


def check_login(username, password):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="voting"
    )

    cursor = db.cursor()

    query = "SELECT * FROM users WHERE username = %s AND password = %s"


    cursor.execute(query, (username, password))

# Fetch the result from the query
    result = cursor.fetchone()

# Close the database connection
    db.close()

# Check if the result is empty or not
    if result is None:
       return False
    else:
       return True


def check_signup(username, password):
    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="voting"
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to check if the username already exists
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))

    # Fetch the result from the query
    result = cursor.fetchone()

    # If the username already exists, return False
    if result is not None:
        return False

    # Execute the SQL query to insert the new user into the database
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))

    # Commit the changes to the database
    db.commit()

    # Close the database connection
    db.close()

    return True


# This function is called when the user clicks on the login button
def check_login_details():
    user = entry_user.get()  # Get the data inside the user entry widget
    passw = entry_passw.get()  # Get the data inside the password entry widget
    # Condition to check if the details entered are correct
    if check_login(user, passw):
        login_stat.config(text="Successfully Logged in!")  # A success message
        messagebox.showinfo('Welcome', "Start to fill the forms")

        root.destroy()
        directory_containing_menu = r"C:\Users\ASA\PycharmProjects\pythonProject80"
        os.chdir(directory_containing_menu)
        os.system('python ASA_menu.py')
    else:
        login_stat.config(text="Invalid username or password")
        messagebox.showerror('sorry', 'Try again')


def sign_up():
    def call_back():
        top.destroy()
        root.deiconify()

    def check_signup_details(usr, pwd):
        user = usr  # Get the data inside the user entry widget
        passw = pwd  # Get the data inside the password entry widget
        # Condition to check if the details entered are correct
        if check_signup(user, passw):
            signup_stat.config(text="Successfully Signed Up!")  # A success message

        else:
            signup_stat.config(text="Invalid username or password")

    root.withdraw()  # Hides the login window
    top = Toplevel()  # create a new Window for signup
    top.geometry("500x400")
    top.configure(bg='blue')                 # Sets the dimension of the window
    top.title("Sign Up Form")  # Sets the title of the window
    Label(root, text='LOGIN HERE', fg='blue', bg='white', font=('Impact', 25, 'bold')).grid(row=0, column=1, pady=20)

    label_user = Label(top, text="Username:", fg='blue', bg='white', font=('Georgia', 15))
    entry_user = Entry(top, width=30)
    label_user.grid(row=1, column=0, padx=10, pady=20)
    entry_user.grid(row=1, column=1, padx=10, pady=20)

    label_passw = Label(top, text="Password:", fg='blue', bg='white', font=('Georgia', 15))
    entry_passw = Entry(top, show="*", width=30)
    label_passw.grid(row=2, column=0, padx=10, pady=10)
    entry_passw.grid(row=2, column=1, padx=10, pady=10)

    button_login = Button(top, text="Sign Up",
                          command=lambda: check_signup_details(entry_user.get(), entry_passw.get()), bg='Blue', fg='White', font=('Impact', 15, 'bold'))
    button_login.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky=E)

    button_signup = Button(top, text="Click here to login", command=call_back, bg='Blue', fg='White', font=('Impact', 15))
    button_signup.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=E)

    # Creating an output display area label, and gridding it to window
    signup_stat = Label(top)
    signup_stat.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


root = Tk()  # Creates a window obect
root.geometry("500x400")  # Sets the dimension of the window
root.title("Login Form")  # Sets the title of the window
root.configure(bg='blue')


label = Label(root, text='LOGIN HERE', fg='blue', bg='white', font=('Impact', 25, 'bold')).grid(row=0, column=1, pady=20)
label_user = Label(root, text="Username:", bg='white', fg='blue', font=('Georgia', 15))
entry_user = Entry(root, width=30)
label_user.grid(row=1, column=0, padx=10, pady=10)
entry_user.grid(row=1, column=1, padx=10, pady=10)

label_passw = Label(root, text="Password:", bg='white', fg='blue', font=('Georgia', 15))
entry_passw = Entry(root, show="*", width=30)
label_passw.grid(row=2, column=0, padx=10, pady=10)
entry_passw.grid(row=2, column=1, padx=10, pady=10)

button_login = Button(root, text="Login", command=check_login_details, bg='Blue', fg='White', font=('Impact', 15, 'bold'))
button_login.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky=E)

button_signup = Button(root, text="click here if you don't have an account", command=sign_up, bg='Blue', fg='White', font=('Impact', 15))
button_signup.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=E)

# Creating an output display area label, and gridding it to window
login_stat = Label(root)
login_stat.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
