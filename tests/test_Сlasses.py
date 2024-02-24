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
def category_1():
    return Category('Спорттовары', 'Товары для спорта', [ball, racket])
@pytest.fixture()
def category_2():
    return Category('Одежда', 'Одежда для спорта', [jacket, shorts, cap])

def test_init(ball):
    assert ball.name == 'Мяч'
    assert ball.quantity == 12

def test_init_Category(category_1):
    assert category_1.name == 'Спорттовары'
    assert category_1.goods == [ball, racket]

def test_count(category_1):
    assert Category.number_of_categories == 2

def test_count(category_2):
    assert Category.number_of_categories == 2

def test_count(category_1):
    assert category_1.goods_quantity == 2

def test_count(category_2):
    assert category_2.goods_quantity == 3