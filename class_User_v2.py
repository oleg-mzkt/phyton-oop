#       Класс Юзер предназначен для создания,записывания в базу данных и поиска пользователей с атрибутами:
# 1. ID - уникальынй номер без повторения 5значное число
# 2. ФИО (Фамилия Имя Отчество) - с возможностью поиска
# 3. Возраст (количество полных лет с автоматическим подсчётом)
# 4. Номер паспорта в формате MP440276
#       Предусмотреть возможность добавления и удаления атрибутов.
#================================================================
class FN_interface:
    
    def __set_name__(self,owner,name):
        self.name = "_" + name
    
    def __get__(self,instance,owner):
        print(f"__get__:{self.name}={owner}")
        return instance.__dict__[self.name]
        
    def __set__(self,instance,value):
        print(f"__set__:{self.name}={value}")
        print(f"__set__:{self.name}={value}")
        instance.__dict__[self.name] = [self.name]

class Full_Name:
    user_name = FN_interface()
    user_surname = FN_interface()
    user_patronymic = FN_interface()
    
    def __init__(self, user_name, user_surname, user_patronymic):
        self.user_name=user_name
        self.user_surname=user_surname
        self.user_patronymic=user_patronymic
    



if __name__=='__main__':
    u=Full_Name(1,2,3)
    print(u.__dict__)
    print(u)
    pass
#================================================================
class Person:
    """Класс персон с атрибуттами ID, ФИО, Возраст, Номер паспорта"""
    S_RUS = 'aбвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()  # заглавные буквы
    NUMBERS ='1234567890'
    
    error_rus = '- может состоять только из русских букв и дефиса'
    error_year = '- год рождения может быть только цыфрами'
    error_id_number = 'ID должен состоять из 5 цыфр'
    error_passport='неверный формат паспорта(XX123456,где XX - серия паспорта, 123456 - номер паспорта)'
    error_passport_serial='неверный ввод серии паспорта (серия паспорта должна состоять из 2ух латинских символов)'
    error_passport_number = 'неверный ввод номера паспорта (серия паспорта должна состоять только из 6-ти цыфр)'
    
    def __new__(cls,*args,**kwargs):
        print ('вызов функции __new__' + str(cls))
        return super().__new__(cls)

    def __init__(self, sname='Фамилия', name='Имя', lname='Отчество', year='Год рождения', id_number='Идентификационный номер', passport='Паспорт:серия,номер'):
        #print('вызов функции __init__' + str(self))
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

    @classmethod
    def verify_sname(cls, sname):
        #print('вызов @classmethod verify_sname')
        if type(sname) != str:
            print(f'"{sname}" {cls.error_rus}')

    @classmethod
    def verify_name(cls, name):
        if type(name) != str:
            print(f'"{name}" {cls.error_rus}')

    @classmethod
    def verify_lname(cls, lname):
        error = '- может состоять только из русских букв и дефиса'
        if type(lname) != str:
            print(f'"{lname}" {cls.error_rus}')

    @classmethod
    def verify_year(cls, year):
        if type(year) != int:
            print(f'"{year}" {cls.error_year}')

    @classmethod
    def verify_id_number(cls, id_number):
        error1_id_number = '- идентификационный номер должен состоять только из цыфр, 5 знаков XXXXX'
        error2_id_number = '- идентификационный номер должен состоять из 5 цыфр'
        if type(id_number) != int:
            print(f'"{id_number}" {error1_id_number}')
        x=str(id_number)

        if len(x) != 5:
            print(f'"{id_number}" {error2_id_number}')

    @classmethod # проверка паспорта корректность
    def verify_passport(cls, passport):
        print(f'вызов функиции verify_passport')
        passport=passport.replace(' ','')
        # print(f'{passport} - удаление пробелов')
        
        if len(passport)!=8:
            print(f'ошибка 1 {cls.error_passport}')

        if len(passport.strip('1234567890')) != 2 :
            x=passport.strip().strip('1234567890')
            print(f'ошибка 2 {x} -  серия паспорта')

        else:
            print(f'ошибка 3 "{passport[0:2]}" {cls.error_passport_serial}')

        # if type(int(passport[2:6])) == int:
        #     print(f'{passport[2:8]} -  номера паспорта')
        #     print(f'"{passport[2:8]}" {cls.error_passport_number}')
        
        if len(passport.strip()) != 6:
            print(f'{passport[2:6]} -  серия паспорта')
            print(f'"{passport}" {cls.error_passport_number}')
        return passport
    
    @property
    def sname(self):
        return self.__sname

    @sname.setter
    def sname(self, sname):
        self.verify_sname(sname)
        self.__sname = sname
    
    @sname.deleter
    def sname(self):
        del (self.__sname)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.verify_name(name)
        self.__name = name
        
    @name.deleter
    def name(self):
        del (self.__name)

    @property
    def lname(self):
        return self.__lname

    @lname.setter
    def lname(self, lname):
        self.verify_name(lname)
        self.__lname = lname
    
    @lname.deleter
    def lname(self):
        del (self.__lname)

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.verify_year(year)
        self.__year = year
    
    @year.deleter
    def year(self):
        del (self.__year)

    @property
    def id_number(self):
        return self.__id_number

    @id_number.setter
    def id_number(self, id_number):
        self.verify_id_number(id_number)
        self.__id_number = id_number
        
    @id_number.deleter
    def id_number(self):
        del (self.__id_number)

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.verify_passport(passport)
        self.__passport = passport

    @passport.deleter
    def passport(self):
        del (self.__passport)
        
    def __del__(self):
        print('удаление экземпляра' + str(self))
    
    def get_old(self):
        return self.__old
    
    def set_old(self, old):
        self.__old=old
    
    def del_old(self):
        del (self.__old)
    
    old = property(get_old,set_old,del_old)

  
    
    # @staticmethod  # - вычисляет возраст
    # def show_old(old): 
    #     old=2024-old
    #     return print('Возраст: '+str(old))
        
if __name__=="__main__":
    X=Person(sname="Корнач", name='Олег', lname='Васильевич', year=1985, id_number=23765, passport=' MP 123456 ')
    # Y=Person(sname="Корнач", name='Олег', lname='Васильевич', year=1984, id_number=23765, passport='MP12345678')
    print('ID:' + str(X.id_number))
    print('Фамилия:' + X.sname)
    print('Имя:'+ X.name)
    print('Отчество:'+ X.lname)
    print('Год рождения:'+ str(X.year))
    X.old=37
    print(X.__dict__)
    del X.old
    print(X.__dict__)
    print(Person)
    #Person.show_old(X.year)   # - для работы со статическим методом 
    # Person.show_old(Y.year)


#print(X.__doc__)

#del (X.passport)

#print(X.__dict__)

# Y = Person(sname='Корнач', name='Олег', lname='Васильевич', year=1985, id_number=23765, passport='MP1234563')
# print(Y.__dict__)

#X.id_number = 1234567890
#X.passprot = ' МР340256 '
#print(X.id_number, X.passprot)
