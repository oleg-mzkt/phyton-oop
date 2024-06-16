class Users:
    "Класс пользователи"
    surname = 'Фамилия'
    name = 'Имя'
    last_name = 'Отчество'
    personal_number = ''
    phone_number = ''
    address = ''
    @classmethod
    def validate(cls,arg):
        print('ВЫЗОВ ВАЛИДЭЙТ')
        return 7<len(cls.surname)<16


    def __new__(cls, *args, **kwargs):
        print('вызов для __new__ lkz '+str(cls))
        return super().__new__(cls)

    def __init__(self,a='Фамилия',b='Имя',c='Отчество'):
        print('вызов инит')
        self.surname=a
        self.name=b
        self.surname=c
    def __del__(self):
        print('удаление экземпляра')

    def set_fio(self, surname):
        self.surname = surname
        return print(self.surname)

us=Users('1','2','3')
print(us)

user1 = Users('Kornach','Oleg','Vasilevich')
user2 = Users('Корнач','Олег','Васильевич')

print(user1.__dict__)
print(user2.__dict__)


class Phones:
    "Класс телефоны"
    model = 'undefined'  # KX-TS2382RUW
    color = 'unknown'  # red
    serial_number = 'None'  #
    invent_muber = 'None'  #
    located = ''  # склад№1/в ремонте/ на раб.месте
    user = ''  # ФИО
    repair = '0'


print('Описание класса:', Phones.__doc__)
i = 0
while i < 3:
    print('введите тлф№', i)
    i += 1;

ph1 = a = Phones()  # класс a
ph2 = b = Phones()  # класс b

print('Phones :', Phones)

print('1', a)
print('2', isinstance(a, Phones))  # >True
print('3', isinstance(b, Phones))  # >True
print('4', type(a))
print('5', a.model)  # >KX-TS2382RUW атрибут класс Phones
print('6', a.color)
print('7', a.serial_number, a.located)
b.model = 'FeTAP791'  # print(b.model_phone)
print('8', b.model)  # >'FeTAP791'
print('9', b.color)
print('10', a.serial_number)

print('11', a.__dict__)  # > NameError: name 'a' is not defined
# print(b.__dict__) # выводит атрибуты класса
setattr(a, 'year', 2024)
print('12', a.__dict__)  # >{}
print('13', dir(a))
setattr(a, 'color', 'red')
setattr(b, 'color', 'green')
print('14', a.color)
print('15', b.color)
print('16', Phones.color)
print(hasattr(Phones, 'color'))
test1 = getattr(a, 'color', False)  # будет возвращать False если указанный атрибут не обнаруживается
print('17  тест 1 = ', test1)  # red
print('18 цвет тфл2', b.color)
delattr(a, 'color')  # удаляем атрибут колор,вместо него будет подставлятся значения атрибуттов класса
test2 = getattr(a, 'color')
print('19  тест 2 =', test2)  # unknown
delattr(Phones, 'color')
test3 = getattr(a, 'color', 'yellow')
print('20  тест 3 =', test3)  # False
print(hasattr(a, 'year'))
print(hasattr(Phones, 'color'))
print(Phones.__dict__)
print(us.surname)
print(us.validate(us.surname))