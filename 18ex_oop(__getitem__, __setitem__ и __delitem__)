# Магические методы ООП
#__getitem__(self,item) - получение значения по ключу item;
#__setitem__(self,key,value) - запись значения value по ключу key;
#__delitem__(self,key) - удаление элемента по ключу key.

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=list(marks)
    
    def __getitem__(self,item):
        if 0<=item<len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")
            
    def __setitem__(self,key,value):
        if not isinstance(key,int) or key<0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")    
        
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)
        
        self.marks[key] = value
    
    def __delitem__(self,key):
        if not isinstance(key,int):
            raise TypeError("Индекс должен быть целым неотрицательным числом")
        del self.marks[key]
        
s1 = Student("Сергей",[5,5,3,2,5])
s1[10] = 4 
print(s1.marks) #>>> [5, 5, 3, 2, 5, None, None, None, None, None, 4]
del s1[10]
print(s1.marks) #>>> [5, 5, 3, 2, 5, None, None, None, None, None]
