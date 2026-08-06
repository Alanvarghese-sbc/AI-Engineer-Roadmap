def cart(**products):

    for product, price in products.items():
        print(f"{product} : {price}")


cart(
    Apple=120,
    Mango=80,
    Orange=100
)