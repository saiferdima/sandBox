a = float(input())
b = float(input())
o = str(input())
if o == "+":
    print(a+b)
if o == "-":
    print(a-b)
if o == "/" and b!=0:
    print(a/b)
if o =="*":
    print(a*b)
if o == "mod" and b!=0:
    print(a%b)
if o == "pow":
    print((a)**b)
if o =="div" and b!=0:
    print(a//b)
if b==0 and (o == "/" or o == "mod" or o == "div"):
    print("Деление на 0!")
   
