class Product:
    def __init__(self, name, price, text, quantity):
        self.name = name
        self.price = price
        self.text = text
        self.quantity = quantity

    def display_product_info(self):
        return f"Name: {self.name}, Price: ${self.price}, Description: {self.text}, Quantity: {self.quantity}"


product = Product("Laptop", 1000, "Powerful gaming laptop", 5)

print(product.display_product_info())



##############################################################

# class Product:
#     def __init__(self, name, price, text, quantity):
#         self.name = name  # Mahsulot nomi
#         self.price = price  # Mahsulot narxi
#         self.text = text  # Mahsulot haqida tavsif
#         self.quantity = quantity  # Mahsulot soni
#
#     # Mahsulot haqidagi barcha ma'lumotlarni ko'rsatadigan metod
#     def display_product_info(self):
#         return f"Name: {self.name}, Price: ${self.price}, Description: {self.text}, Quantity: {self.quantity}"
#
#     # Mahsulot narxini yangilash metodi
#     def update_price(self, new_price):
#         self.price = new_price
#
#     # Mahsulot sonini yangilash metodi
#     def update_quantity(self, new_quantity):
#         self.quantity = new_quantity
#
#     # Mahsulotga chegirma qo'llash
#     def apply_discount(self, discount_percentage):
#         self.price = self.price * (1 - discount_percentage / 100)
#
#
# # Misol uchun Product obyektini yaratish
# product = Product("Laptop", 1000, "Powerful gaming laptop", 5)
#
# # Mahsulot haqida ma'lumot ko'rsatish
# print(product.display_product_info())
#
# # Narxni yangilash va ko'rsatish
# product.update_price(900)
# print("After price update:", product.display_product_info())
#
# # Chegirma qo'llash va ko'rsatish
# product.apply_discount(10)
# print("After discount:", produ
