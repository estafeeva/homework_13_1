from Classes import Product
from Classes import Lawn_grass
from Classes import Smartphone
from Classes import Category

"""
ball = Product('Мяч', 'Футбольный мяч', 300.00, 10)
racket = Product('Ракетка', 'Теннисная ракетка', 3000.00, 20)
jacket = Product('Куртка', 'Куртка детская', 1500.90, 10)
shorts = Product('Шорты', 'Шорты спортивные', 700.20, 2)
cap = Product('Кепка', 'Кепка детская', 250.50, 5)

# Создаем 1-й экземпляр категории и передаем параметры для инициализации
category_1 = Category('Спорттовары', 'Товары для спорта', [ball, racket])
# Создаем 2-й экземпляр категории и передаем параметры для инициализации
category_2 = Category('Одежда', 'Одежда для спорта', [jacket, shorts, cap])


#print(category_1.goods)
data = {'name': 'Шляпа',
        'description': 'Просто шляпа',
        'price': 250.50,
        'quantity': 1}
hat = Product.add_new_product(**data)
print(hat.name)
category_1.add_product(hat)
print(category_1.goods)

racket.price = -5.00
print(racket.price)
print(ball)
print(len(ball))

print(issubclass(Lawn_grass, Product))
grass = Lawn_grass('Газон', 'медленнорастущий газон', 1000.00, 10, "Россия", 3, "салатовый")
category_1.add_product(grass)
print(category_1)
print(len(category_1))
print(grass + grass)

iphone = Smartphone('iPhone', 'телефон', 100000.00, 20, 2, '15', 256, 'white')
iphone.price = -5.00
print(iphone.price)
print(type(grass))
if type(grass) == type(iphone):
        print('да')
else:
        print('нет')"""