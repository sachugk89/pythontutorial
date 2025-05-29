prices={
    "apple":0.50,
    "orange":0.75,
    "milk":1.25,
    "bread":0.45,
    "butter":2.45
}
item1=input("Enter item1 name").lower()
qty1=int(input(f"Enter {item1} qty"))
item2=input("Enter item2 name").lower()
qty2=int(input(f"Enter {item2} qty"))
item3=input("Enter item3 name").lower()
qty3=int(input(f"Enter {item3} qty"))
price1=prices.get(item1,0)
price2=prices.get(item2,0)
price3=prices.get(item3,0)

total1=price1*qty1
total2=price2*qty2
total3=price3*qty3
subtotal=total1+total2+total3
tax=subtotal*0.085
total=subtotal+tax

print("\n-------Receipt-------")
print(f"{item1.capitalize()}:{qty1} @ ${price1:.2f} each=${total1}")
print(f"{item2.capitalize()}:{qty2} @ ${price2:.2f} each=${total2}")
print(f"{item3.capitalize()}:{qty3} @ ${price3:.2f} each=${total3}")
print(f"Subtotal:{subtotal:.2f}")
print(f"Total Tax at 8.5%:{tax}")
print(f"Total Amount:{total}")