x = int(input("Nhập một số n:"))
if x < 0 : 
    exit()
if x > 100 :
    exit
i = 1
for i in range(1 , x+1):
    if x%i == 0:
        print(i)
