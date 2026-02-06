#Restaraunt Management

import os
import qrcode

import datetime
kajur=datetime.datetime.now()

money1=money2=money3=money4=0 #pls ignore this shiii
b=m=c=p=0 #ignore this shiii also

print("---------------Welcome to Raathi restaraunt---------------")
print("                       Greetings!")
print("Heres our menu:-\nBurger=60\nMomo=40\nCoffee=80\nPizza=150")
v = input("Can you tell me your name Sir? :")

items = int(input("how many items you want? :"))
for i in range(items):
    
    while True:
        a = input("WHAT DO YOU WANT? :")

        if a=="burger":
            b = int(input("HOW MUCH QUANTITY YOU WANT? :"))
            money1= 60*b
            break

        elif a=="momo":
            m = int(input("HOW MUCH QUANTITY YOU WANT? :"))
            money2= 40*m
            break

        elif a=="coffee":
            c = int(input("HOW MUCH QUANTITY YOU WANT? :"))
            money3= 80*c
            break

        elif a=="pizza":
            p = int(input("HOW MUCH QUANTITY YOU WANT? :"))
            money4= 150*p
            break

        else:
            print("SORRY SIR! WE DON'T HAVE THIS ITEM")


q="Total Quantity"
p=b+m+c+p
quantity=f"{q} = {p}"
print(quantity)

t="Total Price"
k=money1+money2+money3+money4
total=f"{t} = {k}"
print(total)


while True:
    l = input(f"which payment method do you want cash or upi? your total is {k} : ").strip().lower()

    if l == "upi":
        import qrcode
        img = qrcode.make(f"upi://pay?pa=9927972990@ptsbi&pn=MOHD%20MUNEER&am={k}&tn=Payment")
        img.save(f"{v}.png")
        print("QR code generated")
        break

    elif l == "cash":
        print("ok sir")
        break

    else:
        print("pls choose valid option")

print("---------------------Rathi Rastaraunt----------------------")
print("--------------------------INVOICE--------------------------")
print("   ITEMS                                       QUANTITY")
print("="*59)

if b>0:
    print(f"   BURGER                   :                     {b}")

if m>0:
    print(f"   MOMO                     :                     {m}")

if c>0:
    print(f"   COFFEE                   :                     {c}")

if p>0:
    print(f"   PIZZA                    :                     {p}")

print("="*59)
print(f"   {total}")
print("*"*59)

print(f"Payment Recieved By {l}")

print("*"*59)
print("\t\t   Thankyou for coming")
print("="*59)

print(kajur)
