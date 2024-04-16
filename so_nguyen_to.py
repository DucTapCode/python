def so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# Kiểm tra một số cụ thể
so_can_check = int(input("Nhập số :"))
if so_nguyen_to(so_can_check):
    print(so_can_check, "là số nguyên tố")
else:
    print(so_can_check, "không phải là số nguyên tố")
