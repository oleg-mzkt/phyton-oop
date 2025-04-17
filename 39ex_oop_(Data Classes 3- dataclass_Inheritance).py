#39. Python Data Classes при наследовании | Объектно-ориентированное программирование Python
#  1. создадим базовый класс Goods и наследуемый от него Books(Goods) 
#  через декоратор @dataclass
#  тогда инициализаторы этих классов будут выглядеть след. образом:
# class Goods:
#  def __init__(uid:Any,price:Any=None,weight:Any=None):
#     ... 
#  current_uid = 0 # без аннотации инициализироваться не будет 
#
# class Book(Goods):
#  def __init__(self,uid:Any,price:float=0,int|float=0,title:str="",author:str=""):
#     ...
#  в классе Book будут в инициализатор будут добавлены атрибуты  title и  author в конец т.к. остальные атрибуты наследуются от Goods и они будут переопределены а новые добавляются вконце 
# 

from dataclasses import dataclass, field, InitVar # подгружаем библиотеки с декоратором и функциями
from typing import Any

@dataclass
class Goods:
    current_uid = 0 # без аннотации инициализироваться не будет
    
    uid: Any = field(init=False)
    price: Any = None
    weight: Any = None
    
    def __post_init__(self):       # срабатывает после иницаилизации
        Goods.current_uid += 1
        print(f'Сработал Goods: __post_init__ {Goods.current_uid} раз(а)')
        self.uid = Goods.current_uid

# на основе класса Goods создадим класс Books:
@dataclass
class Book(Goods):
    title: str = "" 
    author: str = "" 
    price: float = 0
    weight: int | float = 0
    
    def __post_init__(self):
        super().__post_init__()
        print(f'Сработал Book: __post_init__')

a = Goods(1)
b = Book(1)   
print(a)
#Goods(uid=1, price=1, weight=None)
print(b)
#Book(uid=2, price=1, weight=0, title='', author='')
b = Book(1000, 100, "Python ООП", "Балакирев С.М.")
print(b)
