class Category:
    """Класс для задания категории."""
    # Переменная на уровне класса для подсчета количества категорий
    number_of_categories = 0

    def __init__(self, name: str, description: str, goods: list):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.goods = goods
        self.goods_quantity = len(goods) #количество товаров в списке одной категории

        """при увеличении количества категорий к переменной 
        number_of_categories обращаемся от класса"""
        Category.number_of_categories += 1

class Product:
    """Класс для задания продукта."""


    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


