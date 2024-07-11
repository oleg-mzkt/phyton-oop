class Users:
    "Класс пользователи"
    surname = 'Фамилия'
    name = 'Имя'
    last_name = 'Отчество'
    id_number = 'Персональный номер'
    pattern ='АБВГДЕЖЗИКЛМ' # надо будет добавить словарь, чтобы проверить правильность ввода ФИО
   # def __new__(cls, *args, **kwargs):
   #     print('вызов для __new__ '+str(cls))
   #     return super().__new__(cls)
    
    def __init__(self,surname:str ,name:str,last_name:str,id_number:int):
        print('Вызов функции инициализации пользователя')
        self.surname=surname
        self.name=name
        self.last_name=last_name
        self.id_number=id_number

    @classmethod
    def set_validate(cls,filtr):
         cls.pattern=filtr
         print('ВЫЗОВ ВАЛИДЭЙТ')

    def __del__(self):
        print('удаление экземпляра')

    def set_user(self,surname:str ,name:str,last_name:str,id_number:int):
        print('запись данных пользователя')
        self.surname = surname
        self.name = name
        self.last_name = last_name
        self.id_number = id_number
        return print('сеттер для ФИО и ID записаны', )
        
    def get_user(self,surname:str ,name:str,last_name:str,id_number:int):
        self.surname = surname
        print('перезаписать данные пользователя ')
        self.surname = surname
        self.name = name
        self.last_name = last_name
        self.id_number = id_number
        return print('сеттер для ФИО и ID записаны')
        
    def __getattribute__(self,item): # функция предназначена для запрета к обращению к (не)существующим атрибутам экземпляра
        print('вызов __getattribute__')
        if item == "Фамилия" or item == "Имя" or item == "Отчество" :
            raise print('недопустимый ввод атрибута')
        else:          
            return object.__getattribute__(self,item)

    def __setattr__(self,key,value):
        print('__setattr__')
        object.__setattr__(self,key,value)
        
user1=Users('Ф','И','О',23267)
user1.NAME=12
f=1
а= isdigit(1)
print(a)
#user1=Users(input(Users.surname+':'),input(Users.name+':'),input(Users.last_name+':'),input(Users.id_number+':'))
#print('имя:',user1.name)

print('распечатаем атрибуты экземляра user1 ', user1.__dict__)
print('распечатаем атрибуты Класса ', Users.__dict__)
###############================########==================###############
class Person:
    S_RUS = 'aбвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper() # заглавные буквы
 
    def __init__(self,sname,name,lname,year,id_number,passport):
        self.verify_fio(sname,name,lname)
        self.verify_year(year)
        self.verify_id_number(id_number)
        self.verify_passport(passport)
        
        self.__sname = sname
        self.__name = name
        self.__lname = lname
        self.__year = year
        self.__id_number = id_number
        self.__passport = passport
      
    @classmethod
    def verify_fio(cls,sname,name,lname):
        error='- может состоять только из русских букв и дефиса'
        if type(sname)!= str:
            print(f'"{sname}" {error}')
        if type(name)!= str:
            print(f'"{sname}" {error}')
        if type(lname)!= str:
            print(f'"{sname}" {error}')
            
    @classmethod
    def verify_year(cls,year):
        error='- год рождения может быть только цыфрами'
        if type(year)!= int:
            print(f'"{year}" {error}')
   
    @classmethod
    def verify_id_number(cls,id_number):
         error='- идентификационный номер может быть только цыфрами'
         if type(id_number)!= int:
             print(f'"{id_number}" {error}')
    
    @classmethod
    def verify_passport(cls,passport):
         error='- серия и номер пасспорт может быть только из первых 2ух латинских букв и 6 цыфр'
         if type(passport)!= str:
             print(f'"{passport}" {error}')
         if len(passport)!=9:
             print(f'"{passport}" {error}')

    @property
    def sname(self):
        return self.__sname
    
    @property
    def name(self):
        return self.__name
    
    @property
    def lname(self):
        return self.__lname
    
    @property
    def year(self):
        return self.__year
   
    @year.setter
    def verify_year(self,year):
        self.__year = year
    
    @property
    def  id_number(self):
        return self.__id_number
    
    @id_number.setter
    def verify_year(self,id_number):
        self.__id_number = id_number
    
    @property
    def  passport(self):
        return self.__passport
    

        

a=Person(sname='Корнач',name='Олег',lname='Васильевич',year=5,id_number=23765,passport='MP123456') 
passport='MP123456'
a.id_number=31354
x=a.id_number
print(x)
