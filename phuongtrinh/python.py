a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
z = b**2 - 4*a*c
if z>0 :
    x = float((-b+z**(1/2))/(2*a))
    y = float((-b-z**(1/2))/(2*a))
    print(x,y)
if z<0:print("phương trình vô nghiệm")
if z==0 :   
    x=y=-b/(2*a)
    print(f"x1=x2={x}")
