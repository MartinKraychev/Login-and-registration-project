from tkinter import *
import json
from tkinter import Tk, font
from tkinter import messagebox
import re


def reset_pass_button(username, answer, passw, passw_conf):
    password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
    for user in users:
        if user['username'] == username:
            if user['answer'] == answer:
                if passw == passw_conf:
                    if re.match(password_pattern, passw):
                        user['password'] = passw
                        with open("db.txt", "w") as file:
                            json.dump(users, file)
                        login_page()
                    else:
                        messagebox.showinfo("Warning!", "Password doesn't match the criteria. ", icon="warning")
                        reset_password()

                else:
                    messagebox.showinfo("Warning!", "Passwords don't match! ", icon="warning")
                    reset_password()

            else:
                messagebox.showinfo("Error!", "Wrong answer to your security question! ", icon="error")
                reset_password()


def go_button(username, entry1, entry2, entry3, entry4):
    global user_data
    if not any(user['username'] == username for user in users):
        messagebox.showinfo("Try again!", "Username doesn't exist!", icon="warning")
        reset_password()
    else:
        for user in users:
            if user['username'] == username:
                user_data_list = [user['password'], user['question'], user['answer']]
                user_data = user_data_list
                entry1.config(state="normal")
                entry1.insert(0, user["question"])
                entry1.config(state="readonly")
                entry2.config(state="normal")
                entry3.config(state="normal")
                entry4.config(state="normal")


def reset_password():
    clear_view()
    tk.configure(bg="SteelBlue1")
    can = Canvas(tk, bg="gold", height=150, width=2500)
    can.place(anchor='n', relx=.6, rely=0)
    label = Label(tk, text="Reset Password", bg="gold")
    label.config(font=("Courier", 36))
    label.place(anchor='center', relx=.5, rely=.1)
    Label(tk, text="Please enter your username here:", bg="SteelBlue1").place(anchor='w', relx=.1, rely=.3)
    username = Entry(tk, width=40)
    username.place(anchor='center', relx=.5, rely=.3)
    Button(tk, text="Go", bg="green", fg="white", height=1, width=2, command=lambda: go_button(username.get(), sec_question, sec_answer, new_password, password_confirmation)).place(
        anchor='w', relx=.7, rely=.3)
    Label(tk, text="Your security question:", bg="SteelBlue1").place(anchor='w', relx=.1, rely=.4)
    sec_question = Entry(tk, state="disabled", width=40)
    sec_question.place(anchor='center', relx=.5, rely=.4)
    Label(tk, text="Type in your answer:", bg="SteelBlue1").place(anchor='w', relx=.1, rely=.5)
    sec_answer = Entry(tk, state="disabled", width=40)
    sec_answer.place(anchor='center', relx=.5, rely=.5)
    Label(tk, text="Select a new password here:", bg="SteelBlue1").place(anchor='w', relx=.1, rely=.6)
    new_password = Entry(tk, show="*", state="disabled", width=40)
    new_password.place(anchor='center', relx=.5, rely=.6)
    Label(tk, text="Confirm the new password:", bg="SteelBlue1").place(anchor='w', relx=.1, rely=.7)
    password_confirmation = Entry(tk, show="*", state="disabled", width=40)
    password_confirmation.place(anchor='center', relx=.5, rely=.7)
    Button(tk, text="Reset password", bg="green", fg="white", height=1, width=15, command=lambda: reset_pass_button(username.get(), sec_answer.get(), new_password.get(), password_confirmation.get())).place(
        anchor='w', relx=.7, rely=.7)

    Button(tk, text="Back to Main Menu", bg="green", fg="white", height=2, width=15, command=render_main_view).place(
        anchor='center', relx=.9, rely=.9)
    Button(tk, text="?", bg="white", fg="black", height=1, width=2, command=pass_hint).place(anchor='w', relx=.7,
                                                                                             rely=.6)


def render_app_view(user):
    clear_view()
    tk.configure(bg="SteelBlue1")
    can = Canvas(tk, bg="gold", height=150, width=2500)
    can.place(anchor='n', relx=.6, rely=0)
    label = Label(tk, text="Home Page", bg="gold")
    label.config(font=("Courier", 36))
    label.place(anchor='center', relx=.5, rely=.1)
    text = f"Welcome to your home page {user}!"
    Label(tk, text=text, bg="SteelBlue1").place(anchor='center', relx=.5, rely=.3)
    Button(tk, text="Sign out", bg="green", fg="white", height=2, width=15, command=render_main_view).place(
        anchor='center', relx=.9, rely=.9)


def login_button(username, password):
    user_found = False
    for user in users:
        if user['username'] == username:
            user_found = True
            if user['password'] == password:
                render_app_view(username)
                break
            else:
                msg = messagebox.askquestion(" Incorrect Password!", "Do you want to reset your password?", icon="warning")
                if msg == "yes":
                    pass
                else:
                    login_page()
                break
    if not user_found:
        msg = messagebox.askquestion("The user doesn't exist!", "Do you want to register?")
        if msg == "yes":
            register()
        else:
            login_page()


def login_page():
    clear_view()
    tk.configure(bg="SteelBlue1")
    can = Canvas(tk, bg="gold", height=150, width=2500)
    can.place(anchor='n', relx=.6, rely=0)
    label = Label(tk, text="Login Menu", bg="gold")
    label.config(font=("Courier", 36))
    label.place(anchor='center', relx=.5, rely=.1)
    Label(tk, text="Enter your details here:", bg="SteelBlue1").place(anchor='center', relx=.5, rely=.4)
    username = Entry(tk, width=40)
    placeholder_text = 'Username'
    username.insert(0, placeholder_text)
    username.bind("<Button-1>", lambda event: clear_entry(event, username))
    username.place(anchor='center', relx=.5, rely=.5)
    password = Entry(tk, show="*", width=40)
    placeholder_text = 'Password'
    password.insert(0, placeholder_text)
    password.place(anchor='center', relx=.5, rely=.55)
    password.bind("<Button-1>", lambda event: clear_entry(event, password))
    Button(tk, text='Login', bg="green yellow", command=lambda: login_button(username.get(), password.get())).place(relx=.38, rely=.6)
    Button(tk, text='Reset password', bg="white", command=reset_password).place(relx=.50, rely=.6)
    Button(tk, text="Back to Main Menu", bg="green", fg="white", height=2, width=15, command=render_main_view).place(
        anchor='center', relx=.9, rely=.9)


def message_window():
    win = Toplevel()
    win.iconbitmap("icon.ico")
    win.configure(bg="SteelBlue1")
    win.title('Username already exists!')
    message = "Do you want to reset your password?"
    win.geometry("400x200")
    Label(win, text=message, bg="gold").pack()
    Button(win, text='Reset password', bg="gold").place(relx=.2, rely=.5)
    Button(win, text='Go back', bg="gold", command=register).place(relx=.6, rely=.5)


def sign_up(username, password, question, answer):
    correct_username = False
    correct_password = False
    username_pattern = r"^[a-zA-Z0-9]{4,16}$"
    password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
    if re.match(username_pattern, username):
        correct_username = True

    if re.match(password_pattern, password):
        correct_password = True

    if correct_password and correct_username:
        if not any(user['username'] == username for user in users):
            user = {"username": username, "password": password, "question": question,
                    "answer": answer}
            users.append(user)
            with open("db.txt", "w") as file:
                json.dump(users, file)
            msg = messagebox.askquestion("Registration Completed",
                                         'Log in now?')
            if msg == "yes":
                login_page()
            else:
                render_main_view()
        else:

            message_window()

    else:
        messagebox.showerror("Error",
                             'Wrong data, please read the hints and try again!')
        register()


def username_hint():
    messagebox.showinfo("Info",
                        'The username must be between 4 and 16 characters. It must contain only digits and letters.')


def pass_hint():
    messagebox.showinfo('Info',
                        'The password must be minimum 8 characters long. It must contain at least one upper case and one lower case letter and at least 1 digits.No other symbols allowed.')


def clear_entry(event, entry):
    entry.delete(0, END)
    entry.unbind('<Button-1>')


def register():
    clear_view()
    options_list = ["In which city you were born?", "Name of your first pet?", "Your mother's first name?",
                    "Favorite sport?"]
    tk.configure(bg="SteelBlue1")
    can = Canvas(tk, bg="gold", height=150, width=2500)
    can.place(anchor='n', relx=.6, rely=0)
    label = Label(tk, text="Registration", bg="gold")
    label.config(font=("Courier", 36))
    label.place(anchor='center', relx=.5, rely=.1)
    username = Entry(tk, width=40)
    placeholder_text = 'Enter a Username'
    username.insert(0, placeholder_text)
    username.bind("<Button-1>", lambda event: clear_entry(event, username))
    username.place(anchor='center', relx=.3, rely=.3)
    Button(tk, text="? ", bg="white", fg="black", height=1, width=2, command=username_hint).place(anchor='center',
                                                                                                  relx=.47, rely=.3)
    Button(tk, text="?", bg="white", fg="black", height=1, width=2, command=pass_hint).place(anchor='center', relx=.47,
                                                                                             rely=.35)
    password = Entry(tk, show="*", width=40)
    placeholder_text = 'Enter a Password'
    password.insert(0, placeholder_text)
    password.place(anchor='center', relx=.3, rely=.35)
    password.bind("<Button-1>", lambda event: clear_entry(event, password))
    value_inside = StringVar(tk)
    value_inside.set("Pick a security question")
    question_menu = OptionMenu(tk, value_inside, *options_list)
    question_menu.config(width=29, font=('Helvetica', 10), bg="white", anchor="w")
    question_menu.place(anchor='center', relx=.3, rely=.4)
    sec_answer = Entry(tk, width=40)
    placeholder_text = 'Answer the question'
    sec_answer.insert(0, placeholder_text)
    sec_answer.place(anchor='center', relx=.3, rely=.45)
    sec_answer.bind("<Button-1>", lambda event: clear_entry(event, sec_answer))
    Button(tk, text="Back to Main Menu", bg="green", fg="white", height=2, width=15, command=render_main_view).place(
        anchor='center', relx=.9, rely=.9)
    Button(tk, text="Sign up", bg="blue", fg="white", height=2, width=15,
           command=lambda: sign_up(username.get(), password.get(), value_inside.get(), sec_answer.get())).place(
        anchor='center', relx=.2, rely=.9)


def clear_view():
    for widget in tk.winfo_children():
        widget.destroy()


def render_main_view():
    clear_view()
    tk.configure(bg="SteelBlue1")
    can = Canvas(tk, bg="gold", height=150, width=2500)
    can.place(anchor='n', relx=.6, rely=0)
    Button(tk, text="Register", bg="white", fg="black", height=2, width=15, command=register).place(anchor='center', relx=.4, rely=.1)
    Button(tk, text="Login", bg="green yellow", fg="black", height=2, width=15, command=login_page).place(anchor='center', relx=.6, rely=.1)


if __name__ == '__main__':
    tk = Tk()
    tk.geometry("1000x600")
    tk.iconbitmap("icon.ico")
    defaultFont = font.nametofont("TkDefaultFont")
    defaultFont.configure(family="times",
                          size=12,
                          weight=font.BOLD)
    try:
        with open("db.txt", "r") as file:
            users = json.loads(file.read())
    except:
        users = []
    user_data = []
    render_main_view()
    tk.mainloop()
