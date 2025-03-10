#34. Метаклассы. Объект type | Объектно-ориентированное программирование Python
# Классы это объекты которые позволяют создвать другие объекты (в том числе и классы).
# Все классы которые создаются пользователем создаются от класса type. 
# Также и класс int, str и др. созданы от класса type

# class A: pass
# print(type(A))
# #>>> <class 'type'>
# print(type(int))
# #>>> <class 'type'>
# print(type(str))
# #>>> <class 'type'>

class Point:
    MAX_COORD = 100
    MIN_COORD = 0
    
    
class B1: pass 
class B2: pass

A = type ('Point', (B1, B2),{'MAX_COORD' : 100,'MIN_COORD' : 0})
print(A)
#>>> <class '__main__.Point'>

pt = A() # создадим экземлпяр класса A() который будет наследоваться сразу от 2х классов  B1 и B2 
print(A.__mro__)
#>>> (<class '__main__.Point'>, <class '__main__.B1'>, <class '__main__.B2'>, <class 'object'>)
print(pt.MAX_COORD) # у экземпляра уже будут атрибуты 'MAX_COORD', 'MIN_COORD'
#>>> 100
