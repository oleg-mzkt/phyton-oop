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
# 4. make_dataclass(cls_name, fields,*,bases=(),namespace=None, init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False,match_args=True,kw_only=False,slots=False,weakref_slot=False)

from dataclasses import dataclass, field, InitVar, make_dataclass # подгружаем библиотеки с декоратором и функциями
from typing import Any


class Car:
    def __init__(self,model,max_speed,price):
        self.model = model
        self.max_speed = max_speed
        self.price = price
        
    def get_max_speed(self):
        return self.max_speed

###########  КЛАССЫ МОЖНО СОЗДОВАТЬ С ПОМОЩЬЮ make_dataclass ########
######### создадим аналог класса Car таким образом #######
# -  make_dataclass используется, как правило, если нужно сформировать класс в процессе выполнения программ, в большенстве случаев используют декоратор @dataclass
CarData = make_dataclass("CarData",
                        [("model",str),"max_speed",("price", float, field(default=0))],
                        namespace={"get_max_speed":lambda self :self.max_speed})
                        # namespace={"название метода":(пример lambda)}
                        #lambda функция - это ф-ция, котор может иметь любое количество аргументов, но вычисляет и возвращает только одно значение ПРИМЕР:
                        #def defined_cube(y):
                        #   return y*y*y
                        #lambda_cube = lambda y: y*y*y 
                        
######## класс созданный таким образом имеет и метод __repr__ и __init__ всё тоже самое что и используюя декоратор @dataclass. ########

d=CarData("BMW 525d",240,4540)
print(d)
print(d.get_max_speed(),'km/h')
print(d.__dict__)
###### убедимся счто в классе присутсвтвует метод(ф-ция)"get_max_speed"

########### dataclass ###########
class GoodsMethodsFactory:  # промежуточный класс 
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
    measure: list = field(default_factory=GoodsMethodsFactory.get_init_measure) #  атрибут длинна ширина высота (список) field(default....)- ссылка на класса с ф-цией для создания списка get_init_measure (если ссылку сразу направить default_factory=Book.... - ничего работать не будет, поэтому нужен промежуточный класс ) 
    
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
c = Book(1000, 100, "Python ООП", "Балакирев С.М.")
print(c)

