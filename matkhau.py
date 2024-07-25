
import random

chucai = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
chuinhoa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
so = ['1','2','3','4','5','6','7','8','9','0']

def taomatkhau(length):
    password = ''
    for _ in range(length):
        if random.randint(0, 1) == 0:
            if random.randint(2,3) == 2:
                password += random.choice(chucai)
            else: password += random.choice(chuinhoa)
        else:
            password += random.choice(so)
    return password

print("Mat khau:" ,taomatkhau(9))