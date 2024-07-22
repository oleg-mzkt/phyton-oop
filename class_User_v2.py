#       Класс Юзер предназначен для создания,записывания в базу данных и поиска пользователей с атрибутами:
# 1. ID - уникальынй номер без повторения 5значное число
# 2. ФИО (Фамилия Имя Отчество) - с возможностью поиска
# 3. Возраст (количество полных лет с автоматическим подсчётом)
# 4. Номер паспорта в формате MP440276
#       Предусмотреть возможность добавления и удаления атрибутов.
# class Interface_Person

class Person:
    """Cоздание пользователя с атрибуттами ID, ФИО, Возраст, Номер паспорта"""
    S_RUS = 'aбвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()  # заглавные буквы
    
    error_rus = '- может состоять только из русских букв и дефиса'
    
    error_year = '- год рождения может быть только цыфрами'
    
    error_id_number = 'ID должен состоять из 5 цыфр'
    
    error_passport_serial='неверный ввод серии паспорта (серия паспорта должна состоять из 2ух латинских символов)'
    error_passport_number = 'неверный ввод номера паспорта (серия паспорта должна состоять только из 6-ти цыфр)'
    

    def __init__(self, sname, name, lname, year, id_number, passport):
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
        if type(sname) != str:
            print(f'"{sname}" {cls.error_rus}')

    @classmethod
    def verify_name(cls, name):
        error = '- может состоять только из русских букв и дефиса'
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
        passport=passport.strip()
        print(f'{passport} удаление пробелов')
        print(f'{passport[0:2]} выделение серии')
        print(f'{passport[2:8]} выделение номера паспорта')
        if type(passport) != str:
            print(f'"{passport[0:2]}" {cls.error_passport_serial}')
        
        if type(passport[2:6]) != str:
            print(f'"{passport[2:6]}" {cls.error_passport_serial}')  
        
        if len(passport) != 8:
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
        
    # def __del__(self):
    #     print('удаление экземпляра' + str(self))



X = Person(sname='Корнач', name='Олег', lname='Васильевич', year=1985, id_number=23765, passport='MP123456 ')
#del (X.passport)

#print(X.__dict__)

# Y = Person(sname='Корнач', name='Олег', lname='Васильевич', year=1985, id_number=23765, passport='MP1234563')
# print(Y.__dict__)

#X.id_number = 1234567890
#X.passprot = ' МР340256 '
#print(X.id_number, X.passprot)
