###-- ДАНДЕР МЕТОДЫ--###
### dunder-методы
#I-часть
# __repr__() - для отображения инф. об объекте класса в режиме отладки в консоле при отладке.
# __str__() - для отображения инф. об объекте класса для пользователей(print,str);
#II-часть
# __len__() - позволяет применять функцию len() к экземплярам класса (длинна,кол-во);
# __abs__() - позволяет применять функцию abs() к экземплярам класса (вычисление моудля).

#I-часть
class Cat:
    """класс котики"""
    def __init__(self,name):
        self.name = name
        
    def __repr__(self):
        return f"{self.__class__}: {self.name}" # отображает имя и класс cat1 в консоле:
                                                #<class '__main__.Cat'>:Васька
        
    def __str__(self):
        return f"{self.name}"                   # отображает имя cat1 для пользователей
        
cat1 = Cat("Васька")
str(cat1)
print(cat1) #>>> Васька

#II-часть
class Point:
    def __init__(self,*args):
        self.coords = args   # введённые *args записываются в список экземпляра.coords
                             # список .coords может быть защищённый .__coords

    def __len__(self):
        return len(self.coords)
    
    def __abs__(self):
        return list(map(abs,self.coords))
    
p= Point (1, -2, -3, 4)
print(p.__dict__)       #>>> {'coords': (1, -2, -3, 4)}
print (len(p))          #>>> 4              (длинна списка p.coords)
print (abs(p))          #>>> [1, 2, 3, 4]
print(abs(p.coords[1])) #>>> 2
print(p.coords[1])      #>>> 1              (выводит из списка значение p.coords[1] )  
