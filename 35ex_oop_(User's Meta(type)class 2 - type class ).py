#35. Пользовательские метаклассы. Параметр metaclass | ООП Python
#1. В Python мы можем создавать свои собственные Метаклассы, которые явно или не явно используют type для создания

#а) с помошью функции 
# (metaclass = craate_class_point) - специальный параметр при создании класса, будет отрабатываться функция craate_class_point
class X: 
    MID_COORD = 50
class Y: pass
class Z: pass 

#Предположим мы бы хотели создавать обхекты класса Point с атрибутами
# class Point:
#     MAX_COORD = 100  
#     MIN_COORD = 0

def create_class_point(name, base, attrs):  # ф-ция дял создания метакласса 
    print(attrs) #  уже автоматически добавлен атрибут get_coords
    base = (X,Y) # так можно наследоваться от других классов
    attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0}) # Метод update() используется для изменения значения имеющегося ключа. Если же ключа нет, то он вместе со значением добавляется в словарь:
    return type(name, base, attrs) # используют type для создания метакласса
     
class Point(metaclass = create_class_point):  # специальный параметр metaclass ссылается на ф-цию создания метакласса
    def get_coords(self):
        return (0, 0)
        
pt = Point()
# когда отрабатывается class Point, name = Point ,base = () кортедж из базовых классов он пустой, и attrs = все атрибуты методы т.е. get_coords + потом ещё добавляем 'MAX_COORD' и 'MIN_COORD' в ф-ции create_class_point( )
print(pt.MAX_COORD)
print(pt.get_coords()) 

print(issubclass(Point,X and Y))
print(issubclass(Point,X and Z))



#б) с помошью  Класса 

class Meta(type): 
    # def __init__(cls,name,base,attrs):
    #     super().__init__(name,base,attrs) # инициализатор базового класса
    #     cls.MAX_COORD = 100
    #     cls.MIN_COORD = 0
# ВМЕСТО def __init__ можно использовать, но атрибуты надо бдует передавать через type.__new__((cls, name, base, attrs))

    def __new__(cls,name,base,attrs):
        attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
        base = (X,Y) # так можно наследоваться от других классов
        return type.__new__(cls, name, base, attrs)



class Point2(metaclass = Meta):  # специальный параметр metaclass ссылается на ф-цию создания метакласса
    def get_coords(self):
        return (0, 0)
        
pt2 = Point2()
print(pt2.MAX_COORD)
print(pt2.MID_COORD)
print(pt2.MIN_COORD)

print(pt2.get_coords()) 

print(issubclass(Point2,X))
print(issubclass(Point2,Y))
# Итог: любой алгоритм можно прописать на уровне классов и на уровне функций, 
# но использование классов позволяет создавать Иерархии + код становиться более читабельным
