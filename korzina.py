class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.user = user
        self.products = {}  # Словник для зберігання товарів і їх кількості

    def add_item(self, item, cnt):
        # Якщо товар вже є в корзині, замінюємо його кількість
        self.products[item] = cnt

    def get_total(self):
        return sum(item.price * cnt for item, cnt in self.products.items())

    def __str__(self):
        items_str = "\n".join(f"{item.name}: {cnt} pcs." for item, cnt in self.products.items())
        return f"User: {self.user}\nItems:\n{items_str}\nTotal: {self.get_total()}"


# Створення товарів
lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
print(lemon)  # lemon, price: 5

# Створення покупця
buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

# Створення замовлення
cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)

# Перевірка
assert isinstance(cart.user, User), 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
cart.add_item(apple, 10)  # Заміна кількості яблук на 10
print(cart)

assert cart.get_total() == 40, 'Повинно залишатися 40!'
