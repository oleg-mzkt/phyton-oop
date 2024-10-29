#Магические методы сравнения 
#+ __eq__() - для равенства ==
# __ne__() - для равенства!=
#+ __lt__() - для равенства <
# __gt__() - для равенства >
#+ __le__() - для равенства <=
# __ge__() - для равенства >=

# для сравнения значений класса а не их id в памяти достаточно переопределить 3 метода 
# __eq__();  __lt__() ;  __le__(); -  остальные методы сравнения просто инвертируются автоматически
# not(__eq__()); not(__gt__()); __ge__() - если они не переопределены.

class Clock:
    __DAY = 86400 # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance (seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY
        
        
    @classmethod
    def __verify_data(cls,other): # метод проверки данных на int или Clock
        if not isinstance(other,(int,Clock)):
            raise TypeError("Операнд справа должен быть тип int или Clock")
        return other if isinstance(other,int) else other.seconds

    def __eq__(self,other): # метод сравнения ==
        sc = self.__verify_data(other)
        return self.seconds == sc
        
    def __lt__(self,other): # метод сравнения <
        sc = self.__verify_data(other)
        return self.seconds < sc 

    def __le__(self,other): # метод сравнения <
        sc = self.__verify_data(other)
        return self.seconds <= sc
        
c1=Clock(1001)
c2=Clock(1000)
c3=c1

print(id(c1))
print(id(c2))
print(id(c3))
print(c1==c2)
print(c1<c3)
print(c1>=c2)

