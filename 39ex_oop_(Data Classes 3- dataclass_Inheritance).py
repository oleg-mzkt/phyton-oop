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
# 2. Инициализаторы базовых классов def __init__() вызываются автоматически , а вот __post_init__() вызывается в том в котором инициализирован... если в дочернем нет - вызывается в базовом классе
# 
# 3. Добавим в класс Book ещё один атрибут measure:list = field() / - будет содержать габариты предметов длина ширина высота
# создадим class GoodsMethodsFactory:
#  Итог: пример использования параметра default_factory
#  это необходимо делать через внешний класс GoodsMethodsFactory т.к. если помещать в этот же клас ссылка  default_factory=Book.get_init_measure) не БУДЕТ РАБОТАТЬ
#
from dataclasses import dataclass, field, InitVar # подгружаем библиотеки с декоратором и функциями
from typing import Any

class GoodsMethodsFactory:
    @staticmethod
    def get_init_measure():
        return[0,0,0] # возращается список из 3ёх значений [длина,выоста,ширин] 

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
    measure: list = field(default_factory=GoodsMethodsFactory.get_init_measure) #  атрибудт длинна ширина высота (список)  ссылка на класса с ф-цией для создания списка get_init_measure
    
######### 4 ########
    # выносим во внешний класс т.к. ссылка:   
    #  default_factory=Book.get_init_measure НЕ БУДЕТ РАБОТАТЬ В ЭТОМ ЖЕ КЛАССЕ
    # @staticmethod
    # def get_init_measure():
    #     return[0,0,0]
    
    def __post_init__(self):    # когда в дочернем классе вызывается __post_init__ в базовом классе он не вызвывается, чтобы явно вызвать нужно использовать функцию super()
        super().__post_init__() # явно вызываем __post_init__ в базовом классе, чтобы проинициализировать инкримент Goods.current_uid += 1
        print(f'Сработал Book: __post_init__')

a = Goods(1)
b = Book(1)   
print(a)
#Goods(uid=1, price=1, weight=None)
print(b)
#Book(uid=2, price=1, weight=0, title='', author='')
b = Book(1000, 100, "Python ООП", "Балакирев С.М.")
print(b)
