# Функция __bool__() в паре с магическим методом __len__() ООП
# Функция bool всегда возвращает true от числе отличных от 0 и false от 0

print(bool(0))        #False
print(bool(123))      #True
print(bool(123.123))  #True
print(bool('123'))    #True

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __len__(self):
        print('__len__')
        return bool(self.x)+bool(self.y)

p1 = Point(0,10)
print('bool-функция для кортежа ',bool(p1),sep=': ',end='!') 
