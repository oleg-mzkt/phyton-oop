#### #14 Магические методы __add__, __sub__, __mul__, __truediv__ | ООП Python ###
class Clock:
    __DAY = 86400 # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance (seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY
        
    def get_time(self):
        s = self.seconds % 60               # секунды 
        m = (self.seconds // 60) % 60       # минуты
        h = (self.seconds // 3600) % 24     # часы
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}" # отображает время в формате h:m:s

    @classmethod
    def __get_formatted(cls,x):
        return str(x).rjust(2,"0")          # ф-ция rjust(s, width) выравнивает ее по правому краю,
                                            # заполняя строку шириной width оставшимися символами s. 
    def __add__(self, other):
        if not isinstance(other, (int, Clock)): 
            raise ArithmeticError("Правый операнд должен быть int или класс Clock")
        sc = other          # вспомогательная переменная для того чтобы можно было провести провеку на Clock
        if isinstance(other, Clock):
            sc= other.seconds
        return Clock(self.seconds + sc)
    
    def __radd__(self, other):  # метод по которому можно прибавлять к целому числу расположенному слева 
        if not isinstance (other, int):
            raise TypeError("Левый операнд должен быть int")
        return self + other     # 500 + clk1
    
    def __iadd__(self, other):  #  метод по которому можно прибавлять в формате clk1 += 100
        print("__iadd__")
        if not isinstance(other, (int,Clock)):
            raise ArithmeticError("Правый операнд должен быть int или объектом класса Clock")
        sc = other          # вспомогательная переменная для того чтобы можно было провести провеку на Clock
        if isinstance(other, Clock):
            sc= other.seconds
        self.seconds + sc
        return self   
        
  
  
    
clk1 = Clock(1000)
print(clk1.get_time())       #>>> 00:16:40
clk2 = Clock(2000)
clk1 = clk1 + 1000
print(clk1.get_time())       #>>> 00:33:20
clk3 = clk1 + clk2
print(clk3.get_time())       #>>> 01:06:40
clk3 = clk3.__add__(0)       #  .__add__() - магический метод __add__
print(clk3.get_time())       #>>> 02:13:20
clk4 = 500 + clk3
print(clk4.get_time())
clk4 += 10 
print(clk4.get_time())
