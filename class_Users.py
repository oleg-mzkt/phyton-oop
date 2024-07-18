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
# Задача:
# Ппрограмма должна вести учёт и движение оборудования от постановки на учёт и до передачи на склад и конкретному пользователю за которым будет закрпелено, до тех пор поко он его не сдаст и оно не будет списано. Программа должна учитывать найменование оборудования, модель, учётный и серийный номера оборудования, место подключения или хранения,а также за кем числится(ФИО и ID)

#class Interface_Person


class Person:
    S_RUS = 'aбвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper() # заглавные буквы
    error='- может состоять только из русских букв и дефиса'
   # error1='неверный ввод серии паспорта (серия паспорта должна состоять из 2ух латинских символов)'
    error2='неверный ввод номера паспорта (серия паспорта должна состоять только из 6-ти цыфр)'
 
    def __init__(self,sname,name,lname,year,id_number,passport):
        self.verify_sname(sname)
        self.verify_name(name)
        self.verify_lname(lname)
        self.verify_year(year)
        self.verify_id_number(id_number)
        self.verify_passport(passport)
        
        self.__sname = sname
        self.__name = name
        self.__lname = lname
        self.__year = year
        self.__id_number = id_number
        self.__passport = passport
    
    def __del__(self):
        print('удаление экземпляра'+str(self))
      
    @classmethod
    def verify_sname(cls,sname):
        if type(sname)!= str:
            print(f'"{sname}" {error}')
    
    @classmethod
    def verify_name(cls,name):
        error='- может состоять только из русских букв и дефиса'
        if type(name)!= str:
            print(f'"{name}" {error}')
    
    @classmethod
    def verify_lname(cls,lname):
        error='- может состоять только из русских букв и дефиса'
        if type(lname)!= str:
            print(f'"{lname}" {error}')
            
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
         if len(passport)!=8:
             print(f'"{passport}" {cls.error2}')

    @property
    def sname(self):
        return self.__sname
        
    @sname.setter
    def sname(self,sname):
        self.verify_sname(sname)
        self.__sname=sname
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.verify_name(name)
        self.__name=name
    
    @property
    def lname(self):
        return self.__lname
        
    @lname.setter
    def lname(self,lname):
        self.verify_name(lname)
        self.__lname=lname
    
    @property
    def year(self):
        return self.__year
   
    @year.setter
    def year(self,year):
        self.verify_year(year)
        self.__year = year
    
    @property
    def  id_number(self):
        return self.__id_number
    
    @id_number.setter
    def id_number(self,id_number):
        self.verify_id_number(id_number)
        self.__id_number = id_number
    
    @property
    def  passport(self):
        return self.__passport
    
    @passport.setter
    def passport(self,passport):
        self.verify_passport(passport)
        self.__passport=passport
    
    @passport.deleter
    def passport(self):
        del(self.__passport)
    
   

        

X=Person(sname='Корнач',name='Олег',lname='Васильевич', year=1985,id_number=23765,passport='MP1234563') 
del (X.passport)

print(X.__dict__)

Y=Person(sname='Корнач',name='Олег',lname='Васильевич', year=1985,id_number=23765,passport='MP1234563') 
print(Y.__dict__)


X.id_number=1234567890
X.passprot='МР340256'
print(X.id_number,X.passprot)
