#38. Введение в Python Data Classes (часть 2) | Объектно-ориентированное программирование Python

##### 1 ###### конструкция декоратора датакласс:

#@dataclass
#class ThingData:
#    name: str       
#    weight: int     
#    price: float = 0
#    dims: list = field(default_factory = list)

##### 1.1 ######  декоратор датакласс, основные ф-ции 

# по умолчанию True : 
# init = [True/False] - в классе объявляется инициализатор __init__
# repr = [True/False] - в классе объявляется маг.метод __repr__
# eq = [True/False] -  в классе объявляется маг.метод __eq__

# по умолчанию False : 
# order = [True/False] - если объявить True, в классе объявляется маг.метод для сравнения <;<=;>;>= (также параметр должен быть eq = True)
# unsafe_hash = [True/False] # влияет на формирования маг.метода __hash__()
# frozen = [True/False] - если объявить True, в классе атрибуты становятся неизменяемыми (можно только проинициализировать один раз)
# slots = [True/False] если объявить True, в классе  атрибуты объявляются в коллекции __slots__

########### Примеры:  
# @dataclass(init=False) - полезно для создания базового класса
# @dataclass(repr=False) = объеты будут ссылаться так <__main__.V3D object at 0x7f7bef34e540> (если бдутем выводить через print)
# @dataclass(eq=True)  - можно сравнивать  print(v == v2)  
# @dataclass(oder=True,eq=True) и oder и eq = True, можем сравнивать <;<=;>;>= (eq по умолч. True)

##### 2 ##### функция  field  и осн. параметры

# часто используемые параметры функции  field (можно загуглить остальные):
# field (init, default_factory, repr, compare, default) 
#  init - булевое значение True/False указывает использовать ли атр. при инициализации объекта - по умолчанию True;
#  default_factory - позволяет создавать некоторые объекты при инициализации и создания объекта класса (default_factory=list - создание пустого списка например)
#  repr -  булевое значение True/False указывает использовать ли атр. в магич. методе __repr__() - по умолчанию True;
#  compare - булевое знач. True/False указывает использовать ли атр. при сравнении объектов - по умолчанию True;
#  default - значения по умолчанию (начальное значение ).




##############################################################################
# Задача: при инициализации параметров формировать вычисляемые свойства как в Vector3D только с помощью @dataclass

from dataclasses import dataclass, field, InitVar # импотриуюем dataclass и ф-цию field и класс InitVar (InitVar как только атрибут (calc_len:InitVar[bool]) анатируем параметр в @dataclass автоматически надо добавить в def post_init )

class Vector3D():
    def __init__(self, x:int, y:int, z:int, calc_len: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x * x + y * y + z * z) ** 0.5 # вычисляется непосредственно  

@dataclass
class V3D:
    x: int = field (repr=False) # не бдует выводиться информация для пользователя по этому атрибуту
    y: int
    z: int = field (compare=False) # позволяет сравнивать объекты без этого атрибута
    calc_len: InitVar[bool] = True
    length: float = field (init=False,compare=False, default = 0) # init=False параметр говорит что не надо инициализировать атрибут "length" и он не будет добавлен при инициализации и не будет являтся параметром при иницилизации и как атрибут не будет сравниваться (compare=False) при сравнении объектов

    def __post_init__(self, calc_len): # маг. метод который делает вычисления после инициализации
        if calc_len: # т.е. изначально length = 0, но если calc_len = True то высчитываем длинну.
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5

v = V3D(1,2,3) # Только три параметра передаёся, а length вычисляется отдельно
print(v)
#>>>V3D(y=2, z=3, length=3.7416573867739413)
v = V3D(1,2,3,False) # Только три параметра передаёся, а calc_len = False 
print(v)
#>>> V3D(y=2, z=3, length=0)
print(v.__dict__)
#>>> {'x': 1, 'y': 2, 'z': 3} но всего три атрибута 

v2 = V3D(1,2,5)
print(v == v2) # сравниваем по 2-ум парамметрам т.к. z: int = field (compare=False) и  length (compare=False)
#>>>V3D(x=1, y=2, z=3, length=3.7416573867739413)
