n = int(input("Nhập n:"))
a = n**(1/2)
if n <0:exit()
elif n > 100:exit()
if n**(1/2) == int(a):
    print(f"{n} là số chính phương")
    print(a)
    A = int(a)
    i = 1
    for i in range(1,A+1):
        if A%i == 0:
            print(i)
else: 
    print("Đây không phải là số chính phương")
    i = 1
    for i in range(1, n +1):
        if n%i==0:
            print(i)