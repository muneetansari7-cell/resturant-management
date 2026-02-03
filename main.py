import os
import qrcode


money1=money2=money3=money4=0 #pls ignore this shiii
b=m=c=p=0 #ignore this shiii also

print("Welcome to Raathi restaraunt")
print("Greetings!")
print("Heres our menu:-\nBurger=60\nMomo=40\nCoffee=80\nPizza=150")
v = input("can you tell me your name sir? :")
items = int(input("how many items you want? :"))
for i in range(items):
    a = input("WHAT DO YOU WANT? :")

    if a=="burger":
        b = int(input("HOW MUCH QUANTITY YOU WANT? :"))
        money1= 60*b

    elif a=="momo":
        m = int(input("HOW MUCH QUANTITY YOU WANT? :"))
        money2= 40*m
    elif a=="coffee":
        c = int(input("HOW MUCH QUANTITY YOU WANT? :"))
        money3= 80*c

    elif a=="pizza":
        p = int(input("HOW MUCH QUANTITY YOU WANT? :"))
        money4= 150*p

    else:
        print("SORRY SIR! WE DON'T HAVE THIS ITEM")

total=money1+money2+money3+money4
print(total)
quantity=b+m+c+p
print(quantity)

print(f"list you've ordered:-\nBurger={b}\nMomo={m}\nCoffee={c}\nPizza={p}")

while True:
    m = input(f"which payment method do you want cash or upi? your total is {total} : ").strip().lower()

    if m == "upi":
        import qrcode
        img = qrcode.make(f"upi://pay?pa=9927972990@ptsbi&pn=MOHD%20MUNEER&am={total}&tn=Payment")
        img.save(f"{v}.png")
        print("QR code generated")
        break

    elif m == "cash":
        print("ok sir")
        break

    else:
        print("pls choose valid option")
