from tkinter import *

def signin():
    un = username_entry.get()
    pw = password_entry.get()
    file = open("login/mktk.txt", "r")
    lines = file.readlines()
    taocap = zip(lines[::2], lines[1::2])
    for username, password in taocap:
            if un == username.strip() and pw == password.strip():
                result_label.config(text="Đăng nhập thành công.")
                login.destroy()
            else:result_label.config(text="Tên người dùng hoặc mật khẩu không chính xác.")

login = Tk()
login.title("Signin")
login.geometry("400x300")

username_label = Label(login, text="Tên người dùng:")
username_label.pack()
username_entry = Entry(login)
username_entry.pack()

password_label = Label(login, text="Mật khẩu:")
password_label.pack()
password_entry = Entry(login, show="*")
password_entry.pack()

login_button = Button(login, text="Đăng nhập", command=signin)
login_button.pack()

result_label = Label(login, text="")
result_label.pack()

login.mainloop()
