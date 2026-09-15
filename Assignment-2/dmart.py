print("\t\t\t D-Mart")

name = input("Name: ")
date = input("Date: ")
print("--------------------------------------------------------")
gender = input("Enter the gender of the customer: ").lower().strip()

print("Item Name\t Quantity \t Price \t Total \t After-Discount")

item1 = input("Item1: ")
quantity1 = int(input())
price1 = 10 * quantity1

if quantity1 > 4:
  discount1 = price1 * 5/100
  final_price1 = price1- discount1

item2 = input("Item2: ")
quantity2 = int(input("Enter the quantity for item2: "))
price2 = 20 * quantity2

item3 = input("Item3: ")
quantity3 = int(input("Enter the quantity for item3: "))
price3 = 30 * quantity3

item4 = input("Item4: ")
quantity4 = int(input("Enter the quantity for item4: "))
price4 = 40 * quantity4

item5 = input("Item5: ")
quantity5 = int(input("Enter the quantity for item5: "))
price5 = 50 * quantity5
discount2 = price5 * 10/100
final_price5 = price5 - discount2

item6 = input("Item6: ")
quantity6 = int(input("Enter the quantity for item6: "))
price6 = 60 * quantity6

item7 = input("Item7: ")
quantity7 = int(input("Enter the quantity for item7: "))
price7 = 70 * quantity7

item8 = input("Item8: ")
quantity8 = int(input("Enter the quantity for item8: "))
price8 = 80 * quantity8

item9 = input("Item9: ")
quantity9 = int(input("Enter the quantity for item9: "))
price9 = 90 * quantity9

item10 = input("Item10: ")
quantity10 = int(input("Enter the quantity for item10: "))
price10 = 100 * quantity10
discount3 = price10 * 15/100
final_price10 = price10 - discount3

print("------------------------------------------------------------")

total_bill = final_price1 + price2 + price3 + price4 + final_price5 + price6 + price7 + price8 + price9 + final_price10

if total_bill > 10000 :
  total_bill = total_bill * 15/100
elif total_bill > 5000 and total_bill < 10000 :
  total_bill = total_bill * 10/100

gst = total_bill * 10/100
total_bill = total_bill + gst
print(f"GST(10%): {total_bill}")


if gender == "female" :
  print("Gift: Cadbury")
else:
 print("Gift: Wallet")

carry_bag = input("Do you want a carry bag?").lower().strip()
if carry_bag == "yes" :
  total_bill = total_bill + 10
  print("yes")
else:
  total_bill = total_bill 

print("-----------------------------------------------------------")

print(f"The total price is: {total_bill}")

print()
print("\t\t Thank You")
print("\t\t To Visit")
print("\t\t D-Mart")


print("----------------------------------------------------------")
    
  









