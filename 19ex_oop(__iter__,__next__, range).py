# Магические методы __iter__ и __next__
# __iter__(self) - получение итератора для перебора объекта;
# __next__(self) - переход к следующему значению и его считываение.
# функция range(start,stop,)- возвращает арифметическую последовательность, значения этой ариф. послед можно перебрать с помощью итератора
a = list(range(5))
print(a)
#print(iter(a)) # а - итерируемый объект

class FRange:
    def __init__(self,start=0.0,stop=0.0,step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
       
    def __iter__(self):
        self.value = self.start - self.step
        #print('возврат на начало ариф.послед.:',self)
        return self
    
    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration

fr = FRange(0,4,1) # fr без функ. __iter__  - не итерируемый объект
# print(next(fr))
# print(fr.__next__())
# print(fr.__next__())
# print(fr.__next__())
# print(next(fr))
# it = iter(fr) #  -после определения ф-ции __iter__ нет ошибки
for x in fr: # после определения функции __iter__() fr - итерируемый
    print(x)
    
    
class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.fr = FRange(start, stop, step)
        
    def __iter__(self):
        self.value = 0
        return self
            
    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration
                
fr = FRange2D(0, 4, 1, 4)
for row in fr:
    for x in row:
        print(x,end = ' ')
    print()
        
