#37. Введение в Python Data Classes (часть 1) | Объектно-ориентированное программирование Python
#1) Декоратор @dataclass - помогает автоматизировать процесс инициализации классов с версии Phyton 3.7+  
# ПРИЕМУЩЕСТВО - сокращается код используя декоратор  @dataclass автоматически используется инициализатор __init__ и  метод __repr__ , который выводи всю информацию в виде ThingData(name='Учебник по Phyton 2', weight=100, price=1024)
#2)  pprint  - можно вывести коллекцию __dict__
# Модуль pprint также предоставляет класс PrettyPrinter, который позволяет создавать объекты с предопределенными настройками форматирования. Это может быть полезно, если вы хотите использовать одинаковые настройки для вывода разных структур данных
#3)  Декоратор @dataclass автоматически прописывает  метод __eq__(), __init__(), __repr__()
# их можно прописать самостоятельно или изменить логигу работы

from dataclasses import dataclass
from pprint import pprint 

class Thing:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        
    def __repr__(self):
        return f"Thing: {self.__dict__}"

########## 1 ##########
        
@dataclass            # декоратор датакласса
class ThingData:
    name: str         # анотация обязательна и важен порядко атрибута
    weight: int       # анотация обязательна и важен порядко атрибута
    price: float      # анотация обязательна и важен порядко атрибута

t = Thing("Учебник по Phyton 1", 100, 1024)
td = ThingData("Учебник по Phyton 2", 100, 1024)

print(t) # стандартный вывод исползуя __repr__():
#>>> Thing: {'name': 'Учебник по Phyton 1', 'weight': 100, 'price': 1024}
print(td) # вывод исползуя декоратор @dataclass
#>>> ThingData(name='Учебник по Phyton 2', weight=100, price=1024) # вывод по порядку

########## 2 ########## from pprint import pprint 
pprint(ThingData.__dict__)

####### 3 #########
td_1 = ThingData("Учебник по Phyton 2", 100, 1024)
td_2 = ThingData("Учебник по Phyton 2", 100, 1024)
print (td_1 == td_2)  # фактически происходит сравнение двух картежей:
                      #(name, weight, price)==(name, weight, price)
#>>> True # объекты равны если равны все параметры (name, weight , price )
#>>> False # объекты не равны если не равен любой параметр (name, weight , price )

# ИТОГ : сравнение возможно т.к. декоратор @dataclass  переопределил магический метод __eq__(): который позволяет сравнение разных объектов
# к примеру можно переопределить для сравнения только по weight не затрагивая параметры, тогда надо в class ThingData: добавить
#  def __eq__(self,other):
#      return self.weight == other.weight


t1 = Thing("Учебник по Phyton 1", 100, 1024)
t2 = Thing("Учебник по Phyton 1", 100, 1024)
print (t1 == t2) 
#>>> False ВСЕГДА т.к. изначально сравнивается id, если не переопределен метод сравнения 
