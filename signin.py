def signin():
    with open("login/mktk.txt", "r") as file:
        un = input("Tên người dùng: ")
        pw = input("Mật khẩu: ")
        lines = file.readlines()
        taocap = zip(lines[::2], lines[1::2])
        for username, password in taocap:
            if un == username.strip() and pw == password.strip():
                print("Đăng nhập thành công.")
                return
        print("Tên người dùng hoặc mật khẩu không chính xác.")
signin()