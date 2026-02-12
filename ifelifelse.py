#task 1
'''a=20
b=40
c=56
if a>b and a>c:
    print("largest a:",a)
elif b>c:
    print("largest b:",b)
else:
    print("largest c:",c)
#task 2
a=91
b=45
c=63
if a<b and a<c:
    print("largest a:",a)
elif b<c:
    print("largest b:",b)
else:
    print("largest c:",c)

#task 3
n=0
if n>0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("zero")'''
#task 4
'''days= int (input("enter the number:"))
if days <=5:
    fine=days*0.40
elif days <=10:
    fine=days*0.65
else:
    fine=days*0.80
print("fine:",fine)'''
#task 5
'''a=int(input("enter the number a:"))
b=int(input("enter the number b:"))
op=input("enter operation(+,-,*,/):")
if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
elif op=='/':
    print(a/b)
else:
    print("invalid opertion")'''
#task 6
'''n=int(input("enter the number:"))
if n%5==0 and n%3==0 and n%7==0:
    print("multiple of 3,5 and 7")
else:
    print("not multiple of 3,5 and 7")'''
#task 7
weight = float(input("Enter weight of parcel in grams: "))
booking = input("Enter booking type ('O' for ordinary, 'E' for express): ").upper()

if weight <= 100:
    charges = 80 if booking == 'O' else 100 if booking == 'E' else 0
elif 101 <= weight <= 500:
    charges = 150 if booking == 'O' else 200 if booking == 'E' else 0
elif 501 <= weight <= 1000:
    charges = 210 if booking == 'O' else 250 if booking == 'E' else 0
else: # weight > 1000
    charges = 250 if booking == 'O' else 300 if booking == 'E' else 0


if charges > 0:
    print(f"Total charges: Rs. {charges}")
else:
    print("Invalid booking type or weight.")


#task 8
'''price=float(input("price of laptop:"))
if price <=50000:
    discount=0
elif price <=100000:
    discount=price*0.10
elif price <=150000:
    discount=price*0.15
else:
    discount=price*0.20
total_price =price-discount
print("price of laptop:",price)
print("discount:",discount)
print("total price:",total_price)'''

      
