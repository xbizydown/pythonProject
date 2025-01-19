class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        current_products = self.get_products().splitlines()
        product_dict = {}

        for line in current_products:
            name, weight, category = line.split(', ')
            product_dict[(name, category)] = float(weight)

        for product in products:
            key = (product.name, product.category)
            if key in product_dict:
                product_dict[key] += product.weight
                print(f"Продукт {product.name} уже был в магазине, его общий вес теперь равен {product_dict[key]}.")
            else:
                product_dict[key] = product.weight

        with open(self.__file_name, 'w') as file:
            for (name, category), weight in product_dict.items():
                file.write(f"{name}, {weight}, {category}\n")


if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    s1.add(p1, p2, p3)
    print(s1.get_products())
