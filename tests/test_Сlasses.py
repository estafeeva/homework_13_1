from Classes import Product
from Classes import Lawn_grass
from Classes import Smartphone
from Classes import Category
import pytest

@pytest.fixture()
def grass():
    return Lawn_grass('Газон', 'медленнорастущий газон', 1000.00, 10, "Россия", 3, "салатовый")

@pytest.fixture()
def iphone():
    return Smartphone('iPhone', 'телефон', 100000.00, 20, 2, '15', 256, 'white')


@pytest.fixture()
def ball():
    return Product('Мяч', 'Футбольный мяч', 300, 10)

@pytest.fixture()
def racket():
    return Product('Ракетка', 'Теннисная ракетка', 3000.00, 20)
@pytest.fixture()
def jacket():
    return Product('Куртка', 'Куртка детская', 1500.90, 10)
@pytest.fixture()
def shorts():
    return Product('Шорты', 'Шорты спортивные', 700.20, 2)
@pytest.fixture()
def cap():
    return Product('Кепка', 'Кепка детская', 250.50, 5)
@pytest.fixture()
def category_1(ball, racket):
    return Category('Спорттовары', 'Товары для спорта', [ball, racket])
@pytest.fixture()
def category_2(jacket, shorts, cap):
    return Category('Одежда', 'Одежда для спорта', [jacket, shorts, cap])


def test_count(category_1, category_2):
    """
    тест - подсчет количества категорий
    """
    assert Category.number_of_categories == 2
    assert category_1.number_of_categories == 2
    assert category_2.number_of_categories == 2


def test_init(ball, iphone):
    """
    тест - корректность инициализации объектов класса Product
    """
    assert ball.name == 'Мяч'
    assert ball.quantity == 10
    assert iphone.efficiency == 2

def test_init_Category(category_1):
    """
    тест - корректность инициализации объектов класса Category
    """
    assert category_1.name == 'Спорттовары'
    assert category_1.goods == '''Мяч, 300 руб. Остаток: 10 шт.\nРакетка, 3000.0 руб. Остаток: 20 шт.\n'''

def test_count_goods(category_1, category_2):
    """
    тест - подсчет количества продуктов
    """
    assert category_1.goods_quantity == 2
    assert category_2.goods_quantity == 3


def test_add_new_product(jacket):
    """
    тест - на создание нового продукта с помощью класс-метода
    """
    data = {'name': 'Куртка',
     'description': 'Куртка детская',
     'price': 1500.90,
     'quantity': 10}
    jacket_2 = Product.add_new_product(**data)
    assert jacket.name == jacket_2.name


def test_change_price(ball, iphone):
    """
    тест - на изменение стоимости продукта (если <= 0, то
    стоимость не меняется, если > 0, то меняется на новое значение
    """
    ball.price = -4
    assert ball.price == 300
    ball.price = 400
    assert ball.price == 400
    iphone.price = -40
    assert iphone.price == 100000

def test_len(ball, category_1, grass):
    assert len(ball) == len("Мяч")
    assert len(grass) == len("Газон")
    assert len(category_1) == 30

def test_add_two_products(ball, racket, jacket, cap, grass, iphone):
    #grass = Lawn_grass('Газон', 'медленнорастущий газон', 1000.00, 10, "Россия", 3, "салатовый")
    assert ball+racket == 63000
    assert grass+grass == 20000
    assert jacket+cap == 16261.50
    assert iphone + iphone == 4000000

def test_is_subclass(grass):
    assert issubclass(Lawn_grass, Product) == True
    assert issubclass(Lawn_grass, Smartphone) == False
    assert isinstance(grass, Lawn_grass) == True

def test_str(ball, grass, category_1, iphone):
    assert str(ball) == f'Мяч, 10 руб. Остаток: 10 шт.'
    assert str(grass) == f'Газон, 10 руб. Остаток: 10 шт.'
    assert str(category_1) == f'Спорттовары, количество продуктов: 30 шт.'
    assert str(iphone) == f'iPhone, 20 руб. Остаток: 20 шт.'