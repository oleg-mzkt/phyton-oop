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
        
user1=Users('Ф','И','О',23267)
user1.NAME=12
f=1
а= isdigit(1)
print(a)
#user1=Users(input(Users.surname+':'),input(Users.name+':'),input(Users.last_name+':'),input(Users.id_number+':'))
#print('имя:',user1.name)

print('распечатаем атрибуты экземляра user1 ', user1.__dict__)
print('распечатаем атрибуты Класса ', Users.__dict__)
