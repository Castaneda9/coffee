"""Этот код предназначен для запуска кофемашины

импортируем библиотеки тайм и tqdm для отображения статус бара"""
import time
from tqdm import tqdm
from pyshortcuts import make_shortcut




def drink():
    """Главная функция для работы"""
    n = int(input('Введите номер напитка: '))
    if n == 1:
        print('Вы выбрали латте.')
    elif n == 2:
        print('Вы выбрали капучино.')
    elif n == 3:
        print('Вы выбрали чай')
    elif n == 4:
        print('Вы выбрали мокко')
    elif n == 5:
        print('Вы выбрали двойной шоколад')
    elif n == 6:
        print('Вы выбрали эспрессо')
    elif n == 7:
        print('Вы выбрали горячее молоко')

    while True:
        """Обрабатываем исключение на случай если вместо денег ввели фальшивки"""
        try:
            pay = int(input("Внесите необходимую сумму: "))
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите числовое значение.")
            continue

        while pay > 0:
            """Если оплата больше ноля она проходит, далее запускаем статус бар"""
            create_drink = True
            compound = ('sugar', 'mixture', 'hot water', 'mix', 'spoon')
            for _ in tqdm(compound, desc='Идёт приготовление', leave=False, ncols=100):
                time.sleep(2)
            print('Готово! Заберите заказ!')
            break
        else:
            while pay == 0:
                print("У вас недостаточно средств")
                pay = int(input("Внесите необходимую сумму: "))
        while True:
            drink()


if __name__ == '__main__':
    drink()
    make_shortcut('/Users/user/PycharmProjects/обучение /main.py',
                  name='Coffee', icon='/Users/user/PycharmProjects/обучение /icona.icns',
                  desktop=True,
                  folder='/Users/user/PycharmProjects/обучение ')
