class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        chosen_list = []
        [chosen_list.append(i) for i in self.products if i[0] == first_letter]
        return chosen_list

    def __repr__(self):
        result = ''
        result += f'Items in the {self.name} catalogue:\n'
        result += '\n'.join(sorted(self.products))
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
