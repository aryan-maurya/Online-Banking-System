# importing needed libraries
import tkinter
import mysql.connector
from tkinter import *
from tkinter import messagebox

# main window
root = Tk()
root.title('Welcome')
root.geometry('600x400')
root.resizable(False, False)


def proceed():
    frametop.destroy()

    frameback = Frame(root, bg="white")
    frameback.place(x=0, y=0, height=400, width=600)

    def cdb():
        try:
            f = open("dbpass.txt", "w")
            f.write(database_pass_entry.get())
            f.close

            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    username="root",  # enter your mySql username
                    password=database_pass_entry.get()  # enter your mySql password
                )

                mycursor = mydb.cursor()

                mycursor.execute("CREATE DATABASE online_multibank_system;")
                mycursor.execute("use online_multibank_system;")
                mycursor.execute(
                    "CREATE TABLE userlist(name varchar(255), mobile_no bigint, email varchar(255), username varchar(255), password varchar(255));")
                mycursor.execute(
                    "create table accounts(name varchar(255), password varchar(255), bank varchar(255), acc_num bigint, balance bigint);")
                messagebox.showinfo("Thankyou", "You may now login...")
                root.destroy()
            except:
                messagebox.showinfo("Warning!",
                                    "Your database password is incorrect, unable to connect.")
        except:
            messagebox.showinfo("Warning!", "You have already completed this process. You can now login.")
            root.destroy()

    # wlcome
    title = Label(frameback, text="Please enter your database password!", font=16, fg='#d77337', bg='white')
    title.place(x=50, y=50)

    # username tag
    database_pass_tag = Label(frameback, text="Password : ", font=('Goudy Old Style', 12, 'bold'), fg='gray',
                              bg='white')
    database_pass_tag.place(x=40, y=100)
    database_pass_entry = Entry(frameback, font=("Times New Roman", 15), bg='lightgray')
    database_pass_entry.place(x=45, y=150, width=250, height=25)

    # Buttons
    submit_button = Button(frameback, text='Submit', font=('Times New Roman', 10, 'bold'), fg='white', bg='#d77337',
                           command=cdb)
    submit_button.place(x=60, y=190)


def halt():
    messagebox.showinfo("Warning!", "You need to setup MySQL in your device to run this project.")


frametop = Frame(root, bg="white")
frametop.place(x=0, y=0, height=400, width=600)

title = Label(frametop, text="Do you have mysql installed in your device?", font=16, fg='#d77337', bg='white')
title.place(x=50, y=50)

YES_button = Button(frametop, text='Yes', font=('Times New Roman', 12, 'bold'), fg='white', bg='#d77337',
                    command=proceed)
YES_button.place(x=50, y=120)
NO_button = Button(frametop, text='No', font=('Times New Roman', 12, 'bold'), fg='white', bg='#d77337', command=halt)
NO_button.place(x=120, y=120)

# end of main window
root.mainloop()
