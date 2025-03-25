#38. Введение в Python Data Classes (часть 2) | Объектно-ориентированное программирование Python

# конструкция декоратора датакласс:

#@dataclass
#class ThingData:
#    name: str       
#    weight: int     
#    price: float = 0
#    dims: list = field(default_factory = list)

# Задача: при инициализации параметров формировать вычисляемые свойства как в Vector3D только с помощью @dataclass

# часто используемые параметры функции  field
# field (init, default_factory, repr, compare, default) 
#  init - булевое значение True/False указывает использовать ли атр. при инициализации объекта - по умолчанию True;
#  default_factory - позволяет создавать некоторые объекты при инициализации и создания объекта класса (default_factory=list - создание пустого списка например)
#  repr -  булевое значение True/False указывает использовать ли атр. в магич. методе __repr__() - по умолчанию True;
#  compare - булевое знач. True/False указывает использовать ли атр. при сравнении объектов - по умолчанию True;
#  default - значения по умолчанию (начальное значение ).

class Vector3D():
    def __init__(self, x:int, y:int, z:int):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x * x + y * y + z * z) ** 0.5 # вычисляется непосредственно  

from dataclasses import dataclass, field
        
@dataclass
class V3D:
    x: int
    y: int
    z: int
    length: float = field (init=False) # init=False параметр говорит что не надо инициализировать атрибут "length" и он не будет добавлен при инициализации и не будет являтся параметром при иницилизации
    
    def __post_init__(self):
        self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5

v = V3D(1,2,3) # Только три параметра передаёся, а length вычисляется
print(v)
#>>>V3D(x=1, y=2, z=3, length=3.7416573867739413)
