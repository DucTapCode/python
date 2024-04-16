#nhập hệ phương trình
print("Ta có hệ phương trình\nax+by=c\nAx+By=C")
a = float(input("Nhập a:"))
b = float(input("Nhập b:"))
c = float(input("Nhập c:"))
A = float(input("Nhập A:"))
B = float(input("Nhập B:"))
C = float(input("Nhập C:"))
print(f"\n{a}x+{b}y={c}\n{A}x+{B}y={C}")
if B>0 and b<0:
    AA = A*(-b)
    CC = C*(-b)
    aa = a*B
    cc = c*B    
    Bb = B*(-b)
    bB = b*B
    print(f"\n{aa}x+{bB}y={cc}\n{AA}x+{Bb}y={CC}")
    Cc = float(CC+cc)
    Aa= float(AA+aa)
    x = Cc/Aa
    y = (c-(a*x))/b
    print(x,y)  
elif B<0 and b>0:
    AA = A*b
    CC = C*b
    aa = a*(-B)
    cc = c*(-B)    
    Bb = B*b
    bB = b*(-B)
    print(f"\n{aa}x+{bB}y={cc}\n{AA}x+{Bb}y={CC}")
    Cc = float(CC+cc)
    Aa= float(AA+aa)
    x = Cc/Aa
    y = (C-A*x)/B
    print(x,y)
elif B<0 and b<0:
    AA = A*(-b)
    CC = C*(-b)
    aa = a*B
    cc = c*B    
    Bb = B*(-b)
    bB = b*B
    print(f"\n{aa}x+{bB}y={cc}\n{AA}x+{Bb}y={CC}")
    Cc = float(CC+cc)
    Aa= float(AA+aa)
    x = Cc/Aa
    y = (c-a*x)/b
    print(x,y)
elif B>0 and b>0:
    AA = A*b
    CC = C*b
    aa = a*(-B)
    cc = c*(-B)    
    Bb = B*b
    bB = b*(-B)
    print(f"\n{aa}x+{bB}y={cc}\n{AA}x+{Bb}y={CC}")
    Cc = float(CC+cc)
    Aa= float(AA+aa)
    x = Cc/Aa
    y = (C-A*x)/B
    print(x,y)
