from Classes import Product
from Classes import Category
import pytest


@pytest.fixture()
def ball():
    return Product('Мяч', 'Футбольный мяч', 350.50, 12)

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


def test_init(ball):
    """
    тест - корректность инициализации объектов класса Product
    """
    assert ball.name == 'Мяч'
    assert ball.quantity == 12

def test_init_Category(category_1):
    """
    тест - корректность инициализации объектов класса Category
    """
    assert category_1.name == 'Спорттовары'
    assert category_1.goods == '''Мяч, 350.5 руб. Остаток: 12 шт.\nРакетка, 3000.0 руб. Остаток: 20 шт.\n'''

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
    jacket_2 = Product.add_new_product('Куртка', 'Куртка детская', 1500.90, 10)
    assert jacket.name == jacket_2.name
