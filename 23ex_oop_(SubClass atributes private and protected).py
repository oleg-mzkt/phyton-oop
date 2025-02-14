#23. Наследование. Атрибуты protected и private | Объектно-ориентированное программирование Python
#1) _attribute (с одним подчеркиванием вначале) - режим доступа protected
#    (служит для обращения внутри класса и во всех его дочерних классах)

#2) __attribute (с двумя подчеркиваниями вначале) - режим доступа private
#    (служит для обращения только внутри класса )

#3) защищать и делать приватными можно и методы используя _ и __ соответственно


#4.1) Итог:

#protected - к протектед атрибутам подклассов можно обращаться через методы _get_coords(self): в родительском классе, если атрибуты определены в родительском, или же через методы _get_coords(self) в дочернем классе, если они определены там.

#private - к приватным атрибутам подклассов можно обращаться через методы get_coords(self): в родительском классе, если атрибуты определены в родительском, если же определить метод get_coords(self) в дочернем классе - бдует ошибка

####################  1   ######################
class Geom():
    name = 'Geom'

    
    def __init__(self,x1,y1,x2,y2,fill='green'):
        print(f'инициализатор Geom для {self.__class__}')
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.__fill = fill

        
    def get_coords(self): # к protected атрибутам подкласса можно обращаться 
        return (self._x1,self._y1)  # через родительский классс и его дочерние классы
        
    def _verify_coord(self,coord): # защищать можно и методы
        return 0 <= coord < 100

    
class Rect(Geom):
    name = 'Rect'
    
    def __init__(self,x1,y1,x2,y2,fill='red'):
        print(f'инициализатор Rect для {self.__class__}')
        super().__init__(x1,y1,x2,y2)
        self._verify_coord(x1)
        self.__fill = fill
    
    def get_coords(self):        
        return (self._x1,self._y1)  #>>> AttributeError: 'Rect' object has no attribute '_Rect__x1'. Did you mean: '_Geom__x1'?


r = Rect(0,0,15,20)
r.get_coords()
print(r._x1)
print(r.name)
print(r.__dict__)
# {'_x1': 0, '_y1': 0, '_x2': 10, '_y2': 20, '_Geom__fill': 'green', '_Rect__fill': 'red'}

# ####################  2   ######################
# class Geom():
#     name = 'Geom'
    
#     def __init__(self,x1,y1,x2,y2):
#         print(f'инициализатор Geom для {self.__class__}')
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2
    
#     def get_coords(self):             # к private атрибутам подкласса можно обращаться 
#         return (self.__x1,self.__y1)  # через родительский классс
#     ###>>> {'_Geom__x1': 0, '_Geom__y1': 0, '_Geom__x2': 10, '_Geom__y2': 20, '_Rect__fill': 'red'}
    
# class Rect(Geom):
#     name = 'Rect'
    
#     def __init__(self,x1,y1,x2,y2,fill='red'):
#         super().__init__(x1,y1,x2,y2)
#         self.__fill = fill
    
#     # def get_coords(self):             # если оставить 
#     #     return (self.__x1,self.__y1)  #>>> AttributeError: 'Rect' object has no attribute '_Rect__x1'. Did you mean: '_Geom__x1'?


# r = Rect(0,0,10,20)
# r.get_coords()
# print(r.__dict__)
