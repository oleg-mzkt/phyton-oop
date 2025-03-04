#31. Инструкция raise и пользовательские исключения | ООП Python
# 1) Мы можем генерировать исключения с помощью комманды raise ZeroDivisionError("своё сообщение")
# - все исключения должны наследоваться от базового класса  BaseException

# 3) генерация своих исключений на примере class MyPrintData:
# - прописать исключения на все случае жизни невозможно

######## 1 ########

print("Test1")
#1/0                    
##>>> ZeroDivisionError: division by zero 
print("Test2")
# raise ZeroDivisionError("деление на ноль") 
##>>> ZeroDivisionError: деление на ноль 
print("Test3")
# a = ZeroDivisionError("деление на ноль")
## raise a #>>> ZeroDivisionError: деление на ноль 
print("Test4")
#raise "деление на ноль" 
##>>> TypeError: exceptions must derive from BaseException
print("Test5")
# x=[1,2,3][4]
## >>>IndexError: list index out of range
print("Test6")

######## 2 ########

# - class Exception(): является базовым для основных ошибок программы и он наследуется от BaseException
# - для обработки исключения, чтобы программа не прерывалась используем 
class PrintData:
    def print(self,data):
        self.send_data(data)
        print(f"идёт печать данных:{str(data)}")
    
    def send_data(self,data):  
        if not self.send_to_print(data): # могут ли данные быть отправлены в принтер ?
            raise Exception("принтер не отвечает")

#>>> Traceback (most recent call last):
#>>>   File "<main.py>", line 47, in <module>
#>>>   File "<main.py>", line 33, in print
#>>>   File "<main.py>", line 38, in send_data
#>>> Exception: принтер не отвечает

        else:
            print("идёт передача данных")
        
    def send_to_print(self,data):
        return 1 # 1/0 данные на принтер отправляются: True/False (да/нет)
print("Test7")        
p = PrintData()
p.print('123')

######## 2 ########
#- создавая собственные исключения мы  можем обрабатывать их
#- можно выстраивать свою собственную ИЕРАРХИЮ исключений - обрабатывая различные ошибки
# Пример:  MyExceptionPrint()←MyExceptionPrintData2()
#- также можно отлавливать их на уровне инициализации 

class MyExceptionPrint(Exception):
    """Общий класс ошибки принтера"""
    
class MyExceptionPrintData2(MyExceptionPrint):
    """Класс исключении при отправке данных принтеру"""
    def __init__(self,*args):
        self.message = args[0] if args else 'Другое сообщение'
        # в переменную self.message будет запсано сообщение с ошибки строка 82 raise MyExceptionPrintData2("принтер2 не отвечает") или None если ничего не будет 
    
    def __str__(self):
        return f"Ошибка:{self.message}"
    
class PrintData2:
    """Класс для печати данных - принтер 2"""
    
    def print(self,data):
        self.send_data(data)
        print(f"идёт печать данных:{str(data)}")
    
    def send_data(self,data):  
        if not self.send_to_print(data): # могут ли данные быть отправлены в принтер ?
            raise MyExceptionPrintData2#("принтер2 не отвечает") # или другое сообщение если параметр передаваемый в *args будет пустым
    
    def send_to_print(self,data):
        return 0 # данные на принтер отправляются: True/False (да/нет)

print("Test8")     
z = PrintData2()
#z.print('456')

#print("Test9")
try:
    z.print('456')
except MyExceptionPrintData2:
    print("ПРИНТЕР2 не отвечает - конструкция try: except:")
try:
    z.print('789')
except MyExceptionPrintData2:
    print ('Иерархия исключения нижний уровень')
except MyExceptionPrint:
    print ('Иерархия исключения верхний уровень - от каких-то других классов исключений')
