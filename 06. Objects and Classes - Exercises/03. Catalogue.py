class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []


    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        return [product for product in self.products if product[0] == first_letter]

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        # result2 = ""
        # for item in (sorted(self.products)):
        #     result2 += f"\n{item}"
        # #result2 = f"{('\n'.join(sorted(self.products)))}"
        # return result + result2
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
