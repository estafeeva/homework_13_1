class Product:
    """Класс для задания продукта."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def add_new_product(cls, **data):
        """Для класса Product добавить метод, который создает товар и возвращает объект,
        который можно добавлять в список товаров.
        Метод принимает словарь данных и использует распаковку аргументов с помощью оператора **"""

        return cls(**data)

    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('цена введена некорректно')
        else:
            self.__price = new_price


class Category:
    """Класс для задания категории."""
    # Переменная на уровне класса для подсчета количества категорий
    number_of_categories = 0

    def __init__(self, name: str, description: str, goods: list[Product]):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__goods = goods
        self.goods_quantity = len(goods) #количество товаров в списке одной категории

        """при увеличении количества категорий к переменной 
        number_of_categories обращаемся от класса"""
        Category.number_of_categories += 1

    def add_product(self, product: Product):
        self.__goods.append(product)


    @property
    def goods(self):  # геттер
        result = ''
        for product in self.__goods:
            result += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return result


