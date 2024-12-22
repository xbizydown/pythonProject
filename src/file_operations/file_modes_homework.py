class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.weight}, {self.category})"

class Shop:
    def __init__(self):
        self.products = []
        self.__file_name = "products.txt"
        self.load_products()

    def load_products(self):
        try:
            with open(self.__file_name, "r") as grocery_product:
                for line in grocery_product:
                    name, weight, category = line.strip().split(", ")
                    self.products.append(Product(name, float(weight), category))
        except FileNotFoundError:
            pass

    def add_product(self, *products):
        for product in products:
            if not any(p.name == product.name and p.weight == product.weight and p.category == product.category for p in self.products):
                self.products.append(product)
            else:
                print(f"Product {product.name} already exists")

    def get_products(self):
        with open(self.__file_name, "w") as grocery_product:
            for product in self.products:
                grocery_product.write(f"{product.name}, {product.weight}, {product.category}\n")
        with open(self.__file_name, "r") as grocery_product:
            return grocery_product.read()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add_product(p1, p2, p3)
print(s1.get_products())
