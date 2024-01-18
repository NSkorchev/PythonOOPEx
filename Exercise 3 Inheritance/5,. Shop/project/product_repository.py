from typing import List

from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        product = next((p for p in self.products if p.name == product_name), None)
        return product

    def remove(self, product_name: str):
        try:
            product = next((p for p in self.products if p.name == product_name), None)
            self.products.remove(product)
        except ValueError:
            return

    def __repr__(self):
        product_info = []
        for product in self.products:
            product_info.append(f"{product}: {product.quantity}")
        return "\n".join(product_info)
