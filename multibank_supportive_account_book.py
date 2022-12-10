# importing needed libraries
import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


# function to hide window
def hide(window):
    window.withdraw()


# function to display window
def show(window):
    window.deiconify()


# function to destroy window
def eliminate(window):
    window.destroy()


# function for login window
def login_page():
    # hidding root window
    hide(root)

    # function for afterlogin
    def loggedin(user, passwd):

        # hidding login window
        hide(login_window)

        # function for logout
        def log_out():
            show(login_window)
            eliminate(logged_in_window)

        # function for adding new account
        def add_acc():

            # creating add account window
            add_acc_window = Toplevel()
            add_acc_window.title("Add account")
            add_acc_window.geometry("500x600")
            add_acc_window.resizable(False, False)
            add_acc_window.config(bg="purple")

            # function for add account button
            def add_account():

                # checking for empty fields
                if bank_name_entry.get() and acc_num_entry.get() and balance_entry.get():

                    # checking username exist or not
                    mycursor.execute("SELECT bank,acc_num FROM accounts WHERE bank = %s and acc_num = %s",
                                     (bank_name_entry.get(), acc_num_entry.get()))
                    result = mycursor.fetchall()
                    flag = 0
                    for i in result:
                        flag = flag + 1

                        # adding new account
                    if flag == 0:

                        # account is unique
                        mycursor.execute("insert into accounts values(%s,%s,%s,%s,%s)", (
                        user, passwd, bank_name_entry.get(), int(acc_num_entry.get()), int(balance_entry.get())))
                        mydb.commit()
                        messagebox.showinfo("Success", "Account added successfully.")
                        eliminate(add_acc_window)

                    else:

                        # account is present
                        messagebox.showinfo("Warning", "Account already present.")

                else:
                    messagebox.showinfo("Warning", "Fill all the details please.")

            # title for add account window
            tag = Label(add_acc_window, text="Add Account", font=30)
            tag.place(x=150, y=50)

            # bank name
            bank_name_label = Label(add_acc_window, text="Bank :", fg="orange", font=12)
            bank_name_label.place(x=100, y=100)
            bank_name_entry = Entry(add_acc_window, font=16)
            bank_name_entry.place(x=100, y=150)

            # account number
            acc_num_label = Label(add_acc_window, text="Account number :", fg="orange", font=12)
            acc_num_label.place(x=100, y=200)
            acc_num_entry = Entry(add_acc_window, font=16)
            acc_num_entry.place(x=100, y=250)

            # balance ammount
            balance_label = Label(add_acc_window, text="Balance :", fg="orange", font=12)
            balance_label.place(x=100, y=300)
            balance_entry = Entry(add_acc_window, font=16)
            balance_entry.place(x=100, y=350)

            # add button
            add_button = Button(add_acc_window, text="ADD", font=12, command=add_account)
            add_button.place(x=100, y=400)

            # add account window end
            add_acc_window.mainloop()

        # function for removing account
        def rev_acc():

            # creating remove account window
            rev_acc_window = Toplevel()
            rev_acc_window.title("Remove account")
            rev_acc_window.geometry("500x600")
            rev_acc_window.resizable(False, False)
            rev_acc_window.config(bg="purple")

            # function for remove button
            def rev_account():

                # checking empty fields
                if bank_name_entry.get() and acc_num_entry.get():

                    # checking account exist or not
                    mycursor.execute("SELECT bank,acc_num FROM accounts WHERE bank = %s and acc_num = %s",
                                     (bank_name_entry.get(), acc_num_entry.get()))
                    result = mycursor.fetchall()
                    flag = 0
                    for i in result:
                        flag = flag + 1

                        # removing account
                    if flag == 1:

                        # account is present
                        mycursor.execute("delete from accounts where bank = %s and acc_num = %s;",
                                         (bank_name_entry.get(), int(acc_num_entry.get())))
                        mydb.commit()
                        messagebox.showinfo("Success", "Account removed successfully.")
                        eliminate(rev_acc_window)

                    else:

                        # account is not present
                        messagebox.showinfo("Warning", "Account does not present.")

                else:
                    messagebox.showinfo("Warning", "Fill all the details please.")

            # title for remove account window
            tag = Label(rev_acc_window, text="Remove Account", font=30)
            tag.place(x=150, y=50)

            # bank name
            bank_name_label = Label(rev_acc_window, text="Bank :", fg="orange", font=12)
            bank_name_label.place(x=100, y=100)
            bank_name_entry = Entry(rev_acc_window, font=16)
            bank_name_entry.place(x=100, y=150)

            # account number
            acc_num_label = Label(rev_acc_window, text="Account number :", fg="orange", font=12)
            acc_num_label.place(x=100, y=200)
            acc_num_entry = Entry(rev_acc_window, font=16)
            acc_num_entry.place(x=100, y=250)

            # remove button
            rev_button = Button(rev_acc_window, text="REMOVE", font=12, command=rev_account)
            rev_button.place(x=100, y=400)

            # remove account window end
            rev_acc_window.mainloop()

        # function for refreshing the data
        def refresh():

            # clearing the accounts frame
            for widget in frame_loggedin.winfo_children():
                widget.destroy()

            # recreating frame column names
            name_of_bank = Label(frame_loggedin, text="Name of Bank", fg="green", bg="white", width=43)
            name_of_bank.grid(row=0, column=0)
            account_number = Label(frame_loggedin, text="Account No.", fg="green", bg="white", width=43)
            account_number.grid(row=0, column=1)
            bank_balance = Label(frame_loggedin, text="Amount", fg="green", bg="white", width=43)
            bank_balance.grid(row=0, column=2)

            # fetching the accounts details from database and displaying in frame
            mycursor.execute("select bank,acc_num,balance from accounts where name = %s and password = %s",
                             (user, passwd))
            result = mycursor.fetchall()
            i = 0
            for person in result:
                for j in range(len(person)):
                    e = Entry(frame_loggedin, width=30, fg="blue", font=12)
                    e.grid(row=i + 1, column=j)
                    e.insert(END, person[j])
                i = i + 1

        # creating afterlogin window
        logged_in_window = Toplevel()
        logged_in_window.title('Welcome')
        logged_in_window.geometry('1199x660+100+50')
        logged_in_window.resizable(False, False)

        # bg image
        logged_in_window.bg = ImageTk.PhotoImage(file='BG.jpg')
        logged_in_window.bg_image = Label(logged_in_window, image=logged_in_window.bg)
        logged_in_window.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

        # getting the user name from database
        mycursor.execute("SELECT name FROM userlist WHERE username = %s and password = %s", (user, passwd))
        name = mycursor.fetchall()

        # passing the username to the label
        name_label = Label(logged_in_window, text="Name :", font=('Times New Roman', 20, 'bold'), bg='lightgrey')
        name_label.place(x=150, y=100)
        uname_label = Label(logged_in_window, text=str(name)[3:-4], font=('Times New Roman', 20, 'bold'), fg="purple",
                            bg='lightgrey')
        uname_label.place(x=250, y=100)

        # creating accounts frame
        frame_loggedin = Frame(logged_in_window, bg='white')
        frame_loggedin.place(x=150, y=150, height=340, width=900)

        # frame column names
        name_of_bank = Label(frame_loggedin, text="Name of Bank", fg="green", bg="white", width=43)
        name_of_bank.grid(row=0, column=0)
        account_number = Label(frame_loggedin, text="Account No.", fg="green", bg="white", width=43)
        account_number.grid(row=0, column=1)
        bank_balance = Label(frame_loggedin, text="Amount", fg="green", bg="white", width=43)
        bank_balance.grid(row=0, column=2)

        # buttons
        logout_button = Button(logged_in_window, text="log out", font=('Times New Roman', 12, 'bold'), fg='white',
                               bg='#d77337', command=log_out)
        logout_button.place(x=1000, y=100)
        add_button = Button(logged_in_window, text=" Add account", font=('Times New Roman', 12, 'bold'), fg='white',
                            bg='#d77337', command=add_acc)
        add_button.place(x=150, y=500)
        remove_button = Button(logged_in_window, text=" Remove account", font=('Times New Roman', 12, 'bold'),
                               fg='white', bg='#d77337', command=rev_acc)
        remove_button.place(x=300, y=500)
        refresh_button = Button(logged_in_window, text=" Refresh", font=('Times New Roman', 12, 'bold'), fg='white',
                                bg='#d77337', command=refresh)
        refresh_button.place(x=450, y=500)

        # after login window end
        logged_in_window.mainloop()

    # function for login button
    def login():

        # checking for empty fields
        if username_entry.get():
            if password_entry.get():

                # all fields are full

                # checking number of entries
                mycursor.execute("SELECT username FROM userlist;")
                numcountresult = mycursor.fetchall()
                count = 0
                for r in numcountresult:
                    count = count + 1

                if count == 0:

                    # no users present
                    messagebox.showinfo("warning", "invalid username/password")

                else:

                    # verifying username and password
                    mycursor.execute("SELECT username,password FROM userlist WHERE username = %s and password = %s",
                                     (username_entry.get(), password_entry.get()))
                    result = mycursor.fetchall()
                    flag = 0
                    for i in result:
                        flag = flag + 1

                    if flag == 0:

                        # wrong username/password entered
                        messagebox.showinfo("warning", "invalid username/password")

                    else:

                        # logged in successfully and logged in funcation called
                        hide(login_window)
                        messagebox.showinfo("success", "You are successfully logged in")
                        loggedin(username_entry.get(), password_entry.get())

            else:

                # password missing
                messagebox.showinfo("warning", "password missing")

        elif password_entry.get():

            # username missing
            messagebox.showinfo("warning", "username missing")

        else:

            # username and password missing
            messagebox.showinfo("warning", "username and password missing")

    # function for back button
    def back():

        # deleting login window and displaying root window
        show(root)
        eliminate(login_window)

    # creating login window
    login_window = Toplevel()
    login_window.title("Login")
    login_window.geometry("1199x660+100+50")
    login_window.resizable(False, False)

    # bg image
    login_window.bg = ImageTk.PhotoImage(file='BG.jpg')
    login_window.bg_image = Label(login_window, image=login_window.bg)
    login_window.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

    # creating login frame
    frame_login = Frame(login_window, bg='white')
    frame_login.place(x=150, y=150, height=340, width=500)

    # title of login frame
    title = Label(frame_login, text="Login", font=('Impact', 36, 'bold'), fg='#d77337', bg='white')
    title.place(x=100, y=20)

    # username
    username_tag = Label(frame_login, text="Username", font=('Goudy Old Style', 12, 'bold'), fg='gray', bg='white')
    username_tag.place(x=40, y=80)
    username_entry = Entry(frame_login, font=("Times New Roman", 15), bg='lightgray')
    username_entry.place(x=45, y=120, width=350, height=35)

    # password
    password_tag = Label(frame_login, text="Password", font=('Goudy Old Style', 12, 'bold'), fg='gray', bg='white')
    password_tag.place(x=40, y=175)
    password_entry = Entry(frame_login, font=("Times New Roman", 15), bg='lightgray')
    password_entry.place(x=45, y=215, width=350, height=35)

    # login button
    login_button = Button(login_window, text='Login', font=('Times New Roman', 24, 'bold'), fg='white', bg='#d77337',
                          command=login)
    login_button.place(x=250, y=450)

    # back button
    back_button = Button(login_window, text='Back', font=('Times New Roman', 24, 'bold'), fg='white', bg='#d77337',
                         command=back)
    back_button.place(x=400, y=450)

    # login window end
    login_window.mainloop()


# function for signup button
def signup_page():
    # hidding root window
    hide(root)

    # function for back button
    def back():

        # deleting signup window and displaying root window
        show(root)
        eliminate(sign_up_window)

    # function for submit button
    def submit():

        # checking all fields are filled
        if fullname_entry.get() or number_entry.get() or email_entry.get() or create_username_entry.get() or password_entry.get():

            # checking number of entries
            mycursor.execute("SELECT username FROM userlist;")
            result = mycursor.fetchall()
            count = 0
            for r in result:
                count = count + 1

            # conditions
            if count > 0:

                # checking username exist or not
                mycursor.execute("SELECT username FROM userlist WHERE mobile_no = %s or username = %s",
                                 (number_entry.get(), create_username_entry.get()))
                result = mycursor.fetchall()
                flag = 0
                for i in result:
                    flag = flag + 1

                    # inserting data
                if flag == 0:

                    # username is unique
                    query = "INSERT INTO userlist (name, mobile_no, email, username, password) values(%s,%s,%s,%s,%s);"
                    mycursor.execute(query, (
                    fullname_entry.get(), int(number_entry.get()), email_entry.get(), create_username_entry.get(),
                    password_entry.get()))
                    mydb.commit()
                    messagebox.showinfo("Success", "you are successfully registered.")
                    # deleting signup window and displaying root window
                    show(root)
                    eliminate(sign_up_window)

                else:

                    # username is present
                    messagebox.showinfo("warning",
                                        "username already exist please try a different username and mobile number.")

            else:

                # if first user
                query = "INSERT INTO userlist (name, mobile_no, email, username, password) values(%s,%s,%s,%s,%s);"
                mycursor.execute(query, (
                fullname_entry.get(), int(number_entry.get()), email_entry.get(), create_username_entry.get(),
                password_entry.get()))
                mydb.commit()
                messagebox.showinfo("Success", "you are successfully registered.")
                # deleting signup window and displaying root window
                show(root)
                eliminate(sign_up_window)

        else:

            # fields are empty
            messagebox.showinfo("warning", "please fill in all the details")

    # creating signup window
    sign_up_window = Toplevel()
    sign_up_window.title('Sign Up')
    sign_up_window.geometry('1199x660+100+50')
    sign_up_window.resizable(False, False)

    # BG image
    sign_up_window.bg = ImageTk.PhotoImage(file='BG.jpg')
    sign_up_window.bg_image = Label(sign_up_window, image=sign_up_window.bg)
    sign_up_window.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

    # creating signup frame
    frame_signup = Frame(sign_up_window, bg='white')
    frame_signup.place(x=150, y=50, height=500, width=700)

    # title of signup frame
    title = Label(frame_signup, text="Sign Up", font=('Impact', 36, 'bold'), fg='#d77337', bg='white')
    title.place(x=170, y=20)

    # name
    fullname_tag = Label(frame_signup, text="Full name", font=('Goudy Old Style', 18, 'bold'), fg='gray', bg='white')
    fullname_tag.place(x=40, y=80)
    fullname_entry = Entry(frame_signup, font=("Times New Roman", 15), bg='lightgray')
    fullname_entry.place(x=40, y=110, width=300)

    # mobile number
    number_tag = Label(frame_signup, text="Mobile number", font=('Goudy Old Style', 18, 'bold'), fg='gray', bg='white')
    number_tag.place(x=40, y=140)
    number_entry = Entry(frame_signup, font=("Times New Roman", 15), bg='lightgray')
    number_entry.place(x=40, y=170, width=300)

    # email
    email_tag = Label(frame_signup, text="Email", font=('Goudy Old Style', 18, 'bold'), fg='gray', bg='white')
    email_tag.place(x=40, y=200)
    email_entry = Entry(frame_signup, font=("Times New Roman", 15), bg='lightgray')
    email_entry.place(x=40, y=230, width=300)

    # username
    nickname_tag = Label(frame_signup, text="Create username", font=('Goudy Old Style', 18, 'bold'), fg='gray',
                         bg='white')
    nickname_tag.place(x=40, y=270)
    create_username_entry = Entry(frame_signup, font=("Times New Roman", 15), bg='lightgray')
    create_username_entry.place(x=40, y=300, width=300)

    # password
    password_tag = Label(frame_signup, text="Password", font=('Goudy Old Style', 18, 'bold'), fg='gray', bg='white')
    password_tag.place(x=40, y=330)
    password_entry = Entry(frame_signup, font=("Times New Roman", 15), bg='lightgray')
    password_entry.place(x=40, y=360, width=300)

    # submit button
    submit_button = Button(sign_up_window, text='Register', font=('Times New Roman', 24, 'bold'), fg='white',
                           bg='#d77337', command=submit)
    submit_button.place(x=350, y=520)

    # back button
    back_button = Button(sign_up_window, text='Back', font=('Times New Roman', 24, 'bold'), fg='white', bg='#d77337',
                         command=back)
    back_button.place(x=500, y=520)

    # signup window end
    sign_up_window.mainloop()


# function for about button
def about_page():
    # hidding root window
    hide(root)

    # creating about window
    about = Toplevel()
    about.title('About')
    about.geometry('1199x660+100+50')
    about.resizable(False, False)

    # BG image
    about.bg = ImageTk.PhotoImage(file='BG.jpg')
    about.bg_image = Label(about, image=about.bg)
    about.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

    # function for back button
    def back():
        # deleting about window and dislpaying root window
        show(root)
        eliminate(about)

    # title for about frame
    text = Label(about,
                 text="We are one of\nIndia's finest bank\nServices providing\nonline security\nand storing your\ncredentials in our\nsecured databse.",
                 font=('Times New Roman', 24, 'normal'), fg='orange')
    text.pack()

    # back button
    back_button = Button(about, text="Back", font=('Times New Roman', 12, 'bold'), fg='white', bg='#d77337',
                         command=back)
    back_button.place(x=900, y=20)

    about.mainloop()


# START OF THE PROGRAM...

# creating root/main window
root = Toplevel()
root.title('Welcome')
root.geometry('1199x660+100+50')
root.resizable(False, False)

# Making DATABASE CONNECTION
try:

    # getting the password of the databse from file created by runme file
    f = open("dbpass.txt", "r")
    pwd = f.readline()
    f.close()

    # connection
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=pwd, database="online_multibank_system")
    mycursor = mydb.cursor()
    # success

except:

    # if runme file is not executed before
    messagebox.showinfo("warning", "Execute the runme file first")
    root.destroy()

# bg image
root.bg = ImageTk.PhotoImage(file='BG.jpg')
root.bg_image = Label(root, image=root.bg)
root.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

# title for welcome
title = Label(root, text="Welcome to India's Finest Bank Services", font=('New Times Roman', 26, 'bold'), fg='#d77337',
              bg='white')
title.place(x=250, y=50)

# Buttons
signup_button = Button(root, text='Sign Up', font=('Times New Roman', 22, 'bold'), fg='white', bg='#d77337',
                       command=signup_page)
signup_button.place(x=250, y=125)
login_button = Button(root, text='Login', font=('Times New Roman', 22, 'bold'), fg='white', bg='#d77337',
                      command=login_page)
login_button.place(x=525, y=125)
about_button = Button(root, text='About Us', font=('Times New Roman', 22, 'bold'), fg='white', bg='#d77337',
                      command=about_page)
about_button.place(x=750, y=125)

# end of main window
root.mainloop()
