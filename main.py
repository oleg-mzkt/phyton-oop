class Users:
    "Класс пользователи"
    surname = 'Фамилия'
    name = 'Имя'
    last_name = 'Отчество'
    personal_number = ''
    phone_number = ''
    address = ''

    def set_fio(self, surname):
        self.surname = surname
        return print(self.surname)


user1 = Users()
user2 = Users()
user1.set_fio('Корнач')

print(user1.surname)


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