from abc import ABC, abstractmethod

class MixinPrint:
    """миксин для логирования информации о создаваемом объекте"""

    def __init__(self):
        print(f'Создан объект {repr(self)}')

    def __repr__(self):
        k1 = ""
        k2 = ", "
        i = 0
        for value in self.__dict__.values():
            i += 1
            if i <= len(self.__dict__.values())-4:
                k2 += f'{value}, '
            else:
                k1 += f'{value}, '

        return f'{self.__class__.__name__}({k1[:-2]}{k2[:-2]})'


class BaseProduct(ABC):
    """
    общий абстрактный класс для всех продуктов;
    выделен общий функционал, который должен быть у каждого продукта,
    и описан в абстрактных методах
    """
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

class Product(MixinPrint, BaseProduct):
    """Класс для задания продукта."""

    def __init__(self, name: str, description: str, price: float, quantity: int):

        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

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

    def __str__(self):
        """Название продукта, 80 руб. Остаток: 15 шт."""
        return f'{self.name}, {self.quantity} руб. Остаток: {self.quantity} шт.'

    def __len__(self):
        return len(self.name)

    def __add__(self, other):
        """функция сложения продуктов, проверяет, чтобы можно было
        складывать товары только из одинаковых классов продуктов."""
        if type(self) == type(other):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("Можно складывать товары только из одинаковых классов продуктов")


class Smartphone(Product):
    """Смартфон - класс-наследник класса Продукты"""
    def __init__(self, name, description, price, quantity, efficiency: int, model, memory, color):

        self.efficiency = efficiency
        self.model = model
        self.memory = memory #объем встроенной памяти
        self.color = color
        super().__init__(name, description, price, quantity)

class Lawn_grass(Product):
    """Газоная трава - класс-наследник класса Продукты"""
    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, period: int, color: str):

        self.country = country
        self.period = period
        self.color = color
        super().__init__(name, description, price, quantity)

class Category(MixinPrint):
    """Класс для задания категории."""
    # Переменная на уровне класса для подсчета количества категорий
    number_of_categories = 0

    def __init__(self, name: str, description: str, goods: list[Product]):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__goods = goods
        super().__init__()
        self.goods_quantity = len(goods) #количество товаров в списке одной категории


        """при увеличении количества категорий к переменной 
        number_of_categories обращаемся от класса"""
        Category.number_of_categories += 1

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__goods.append(product)
        else:
            raise TypeError("Добавить можно только элемент класса Product")


    @property
    def goods(self):  # геттер
        result = ''
        for product in self.__goods:
            result += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return result

    def __str__(self):
        """Название категории, количество продуктов: 200 шт."""

        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def __len__(self):
        """для подсчета количества продуктов в категории"""
        i = 0  # переменная для подсчета продуктов в категории
        for good in self.__goods:
            i += good.quantity
        return i
