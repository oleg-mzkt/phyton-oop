#27. Как работает __slots__ с property и при наследовании | ООП Python

# 1) Использование __slots__() ограничевает создание локальных свойств, но не атрибуты самого класса, поэтому можно создавать свойства @property и .setter .getter если они определены в __init__()


# 2) наследование  __slots__

######### 1 ########

class Point2D():
    __slots__ = ('x','y', '__length' ) # в объектах Point2D выделяются только 2-а локальных свойства(x и y) - никакие другие
    def __init__(self,x,y):
        self.x = x 
        self.y = y
        self.__length = int((x*x+y*y)**0.5) # или любое другое определение __length
    
    @property
    def length(self):
        return self.__length
        
    @length.setter
    def length(self,value):
        self.__length = value

pt = Point2D(3,4)
print(pt.length)
pt.length = 10
print(pt.length)

######### 2 ########

class Point3D(Point2D):
    __slots__ = ('z') # добавляем к наследуемым атрибутам 'x' 'y' '__length'  ещё и 'z'
    
    def __init__(self,x,y,z):
        self.x = x 
        self.y = y
        self.z = z 
    
pt3 =  Point3D(1,2,30)
pt3.length = 500
print(pt3.x, pt3.y, pt3.z, pt3.length)
# >>> 1 2 30 500 
# но мы попрежнему не можем создавать локальные аттрибуты pt3.length2 = 1000 # ERROR
