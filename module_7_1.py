from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        return file.read()
        file.close()

    def add_product(self, *products):
        file = open(self.__file_name, 'a')
        for product in products:
            if product.name and product.category not in file.read():
                file.write(f'\n{product}')
        file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Orange', 5.5, 'Fruits')

print(p2)
print(p1)

s1.add_product(p1, p2, p3)
#
# print(s1.get_products())

