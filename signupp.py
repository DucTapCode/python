from tkinter import *

def signup():
    un = username_entry.get()
    pw = password_entry.get()
    if len(un) >= 9 or len(pw) >= 9:
            result_label.config(text="Ít hơn 9 ký tự")
    else:
            x.write(f"{un}\n")
            x.write(f"{pw}\n")
            result_label.config(text="Đăng ký thành công.")
            login.destroy()

login = Tk()
login.title("Signup")
login.geometry("400x300")

username_label = Label(login, text="Tên người dùng:")
username_label.pack()
username_entry = Entry(login)
username_entry.pack()

password_label = Label(login, text="Mật khẩu:")
password_label.pack()
password_entry = Entry(login, show="*")
password_entry.pack()

signup_button = Button(login, text="Đăng ký", command=signup)
signup_button.pack()

result_label = Label(login, text="")
result_label.pack()

x = open("login/mktk.txt", "a+")

login.mainloop()
