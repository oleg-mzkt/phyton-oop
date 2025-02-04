# Насследование пользовательских классов происходит от базового класса object
#1) object⭠Geom⭠Line⭠ и т.д.
#2) issubclass(класс1,класс2) - ф-ция определение наследования класса (аргументы ф-ции могут быть только классы)
#3) класс int также наследуется от базового класса object ( list float dict tuple и т.д. )
#4) isinstance(объект,Line)  - определение принадлежности объекта к классу (аргументы могут быть как классы так и объекты)
#5) Можно расширять работу стандартных классов в подклассе например класса list. 
#а) Т.е. благодоря тому что list является классом можем наследоваться от него и переопределить вывод метода __str__(self):. 
#б) а тип этого класса становиться уже не лист а '__main__.Vecotr'

########## 1 ###########
class Geom:
    pass
x= Geom()
class Line(Geom):
    pass
########## 2 ###########
print(issubclass(Geom,object)) # issubclass(класс1,класс2) - ф-ция определение наследования класса 
print(issubclass(Line,Geom)) #True
print(issubclass(Geom,Line)) #False

########## 3 ###########
print(issubclass(Line,object)) #True
print(issubclass(int,object)) #True - ps/ list float dict tuple и т.д. 

########## 4 ###########
print(isinstance(x,Geom)) #True
print(isinstance(x,Line)) #False
print(isinstance(Line,Geom)) #True

########## 5 ###########
class Vector(list):
    def __str__(self):
        return "+".join(map(str,self)) # переопределяем вывод
## 5а ##
v = Vector([1,2,3]) #1+2+3
print(v)
## 5б ####
print(type(v)) #<class '__main__.Vector'>
