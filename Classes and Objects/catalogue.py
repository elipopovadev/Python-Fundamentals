class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)
    
    def get_by_letter(self, first_letter):
        new_list = []
        for product in self.products:
            if product.startswith(first_letter):
                new_list.append(product)
        return new_list   
         
    def __repr__(self):
        result = []
        result.append(f"Items in the {self.name} catalogue:")
        for product in sorted(self.products):
            result.append(product)
        return "\n".join(result)


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
