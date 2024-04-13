from tkinter import *
x = open("login/mktk.txt" , "a+")
def signup():
    un = input("Tên người dùng: ")
    pw = input("Mật khẩu: ")
    if len(un)>8 or len(pw)>8:
        print("Ít hơn 9 ký tự")
        exit
    else:
        x.write(f"{un}\n")
        x.write(f"{pw}\n")
signup()