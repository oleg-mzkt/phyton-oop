class Users:
    "Класс пользователи"
    surname = 'Фамилия'
    name = 'Имя'
    last_name = 'Отчество'
    id_number = 'Персональный номер'
    phone_number = 'Номер телефона'

    def __init__(self,surname:str ,name:str,last_name:str,id_number:int):
        print('вызов инит')
        self.surname=surname
        self.name=name
        self.last_name=last_name
        self.id_number=id_number

    @classmethod
    def validate(cls,arg):
        print('ВЫЗОВ ВАЛИДЭЙТ')
        return 7<len(cls.surname)<16

    def __new__(cls, *args, **kwargs):
        print('вызов для __new__ lkz '+str(cls))
        return super().__new__(cls)


    def __del__(self):
        print('удаление экземпляра')

    def set_fio(self, surname):
        self.surname = surname
        return print(self.surname)

user1=Users(input(Users.surname+':'),input(Users.name+':'),input(Users.last_name+':'),input(Users.id_number+':'))
print('имя:',user1.surname)



print('распечатаем атрибуты экземляра user1 ', user1.__dict__)
