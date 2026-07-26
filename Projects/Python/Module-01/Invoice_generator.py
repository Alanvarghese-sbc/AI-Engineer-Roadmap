# Mini Project: Invoice Generator

customer = input("Enter customer name: ")
product = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("==========================")
print("INVOICE")
print("==========================")
print()
print(f"Customer : {customer}")
print(f"Product  : {product}")
print(f"Price    : ${price:.0f}")
print(f"Quantity : {quantity}")
print()
print(f"Total    : ${total:.0f}")