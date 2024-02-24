class Category:
    """Класс для задания категории."""
    name: str
    description: str
    goods: list

    # Переменная на уровне класса для подсчета количества категорий
    number_of_categories = 0

    def __init__(self, name, description, goods):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.goods = goods
        self.goods_quantity = len(goods)

        Category.number_of_categories += 1

class Product:
    """Класс для задания продукта."""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


