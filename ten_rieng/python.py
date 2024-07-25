def chinh_sua_va_dem_ten(ten):
    tudau = ten[0].upper()
    so_tu = 1  # Khởi tạo số từ là 1 vì tên đầu tiên không cần dấu cách để ngăn cách
    for i in range(1, len(ten)):
        if ten[i].isupper():
            tudau += " " + ten[i]
            so_tu += 1
        else:
            tudau += ten[i]
    return tudau, so_tu
ten_nhap_vao = input("")
ten_da_chinh_sua, so_tu = chinh_sua_va_dem_ten(ten_nhap_vao)
print(ten_da_chinh_sua)
print(so_tu)
