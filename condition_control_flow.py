# WAP to apply the amount of discount a restaurant applies based on the amount spent by the customer.

bill_total = 298
discount1 = 10
discount2 = 20

if bill_total > 200:
    print("Bill total is greater than $200")
    bill_total = bill_total - discount2
elif bill_total > 100 and bill_total < 200:
    print("Bill total is greater than $100 and less than $200")
    bill_total = bill_total - discount2
else:
    print("Bill total is less than $100")

print(f"Bill total : ${bill_total}")
