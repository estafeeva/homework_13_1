from Classes import Product
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

print(category_2)
print(len(category_2))
print(ball + racket)
"""