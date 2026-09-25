class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class Bill:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.total_price()
        return total

    def calculate_tax(self, total):
        return total * 0.18

    def display_bill(self):
        total = self.calculate_total()
        tax = self.calculate_tax(total)
        final_total = total + tax

        print("\n--- BILL ---")
        print("Product\t\tPrice\tQty\tTotal")

        for product in self.products:
            print(product.name, "\t", product.price, "\t",
                  product.quantity, "\t", product.total_price())

        print("\nSubtotal:", total)
        print("Tax (18%):", round(tax,2))
        print("Final Total:", final_total)


bill = Bill()

bill.add_product(Product("Notebook", 50, 2))
bill.add_product(Product("Pen", 10, 3))
bill.add_product(Product("Bag", 500, 1))

bill.display_bill()