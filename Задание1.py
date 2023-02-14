
from decimal import Decimal
import time
from typing import Literal, TypeVar

SelfTechnic = TypeVar("SelfTechnic", bound="Technic")


class Technic:
    # Стоимость дял товаров, ниже которой, он будет относиться к "Бюджетной" категории
    cost_budget: Decimal = Decimal("1000")

    __slots__ = ("name", "availability", "__cost", "__category_by_cost")

    def __init__(self, name: str, cost: Decimal, availability: bool):
        # название
        self.name: str = name
        # наличие (True, False)
        self.availability: bool = availability
        # цена
        self.__cost: Decimal = cost
        # Категория товара
        self.__category_by_cost: Literal[
            '«Бюджетный»',
            "«Дорогой»"
        ] = self.__f_category_by_cost()

    ##
    #
    ##

    @property
    def cost(self) -> Decimal:
        return self.__cost

    @property
    def category_by_cost(self) -> Literal['«Бюджетный»', "«Дорогой»"]:
        return self.__category_by_cost

    @category_by_cost.setter
    def category_by_cost(self): ...

    @cost.setter
    def cost(self, values: Decimal):
        self.__cost = values
        self.__category_by_cost = self.__f_category_by_cost()

    def __f_category_by_cost(self):
        """
        По цене определить товар в категорию 

        cost: Цена
        return: «Бюджетный» / «Дорогой»
        """
        return '«Дорогой»' if self.__cost > self.cost_budget else "«Бюджетный»"

    def __eq__(self, obj: SelfTechnic):
        return len(self.name) == len(obj.name)


def P1():
    """
    1. Необходимо создать класс «Technic» с тремя параметрами:
    название, цена, наличие (True, False). 

    С помощью тернарного
    оператора по цене определить товар в категорию
    «Бюджетный» / «Дорогой».

    *Важно, необходимо ограничить добавление других наборов атрибутов и методов. 
    """
    # 1. Создаем класс для хранения товара
    product = Technic('GeForce RTX 4070', Decimal('79_999.98'), False)

    # По цене определить товар в категорию
    """
    Я использовал get/set для автоматической определение категории товара при изменение цены у объекта
    """
    # '«Дорогой»'
    print(product.category_by_cost)
    # Изменяем цену
    product.cost = Decimal('800')
    # Также изменяется категория на '«Бюджетный»'
    print(product.category_by_cost)

    # *Важно, необходимо ограничить добавление других наборов атрибутов и методов.
    try:
        product.Another = None
    except AttributeError:
        print('Нельзя добавлять атрибуты в класс')


def execute_time(fun):
    """Декоратор для замера времени выполнения функции"""
    def wrapper(*arg, **kwargs):
        start = time.process_time()
        res = fun(*arg, **kwargs)
        end = time.process_time()
        print(end - start)
        return res
    return wrapper


@execute_time
def P2():
    """
    2. На основе предыдущего задания необходимо выполнить
    сравнение строк «Названия техники» по количеству символов,
    неиспользованный скрипт закомментировать.
    *воспользоваться магическими методами;
    ** воспользоваться декоратором.
    """
    # 1. Создаем класс для хранения товара
    list_product_raw = (
        ('GeForce RTX 4060', Decimal('70_999.98'), False),
        ('GeForce RTX 4070', Decimal('79_999.98'), False),
        ('GeForce RTX 4080', Decimal('89_999.98'), False),
        ('GeForce RTX 4090', Decimal('99_999.98'), False),
        ('GeForce RTX 3070 TI', Decimal('59_999.98'), True),
    )
    list_product_obj = [Technic(*x) for x in list_product_raw]

    # Равны
    print(list_product_obj[0] == list_product_obj[1])
    # Не равны
    print(list_product_obj[0] == list_product_obj[-1])


if __name__ == "__main__":
    P1()
    P2()
