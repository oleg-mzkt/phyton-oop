#33. Вложенные классы.  Объектно-ориентированное программирование Python.
# с помощью вложенных классов можно создовать таблицы и подтаблицы с возможностью сортировки данных.

class Women:
  title = 'объект класса для поля title'
  photo = 'объект класса для поля photo'
  ordering = 'объект класса для поля ordering'   # атрибут
  
  def __init__(self,user,passworld):
    self.user = user
    self.passworld = passworld
    self.meta = self.Meta(user+'@'+passworld)    # строчка позволяющая создавать объект класса Meta (+ теперь нужен иннициализатор для объекта класса Meta)

  class Meta:                                    # вложенный класс
    ordering = ['id'] # параметр id который управляет сортировкой данных (т.е. таблица в таблице)
    def __init__(self, access):
        self.access = access

print(Women.ordering)       # обращение к атрибуту ordering класса Women
print(Women.Meta.ordering)  # обращение к полю ordering класса Women вложенного класса Meta
# таким образом можно создавать вложенные таблицы

w= Women('root','12345') # создадим объект класса Women (прописываем инициализацию для класса Meta тоже + Women __init__ необходимо  self.meta = self.Meta(user+'@'+passworld), где  user+'@'+passworld, параметры которые необходимо указывать при создании объекта 'w'  user и passworld )

print(w.ordering)       # обращение к атрибуту объекта w 
#>>> объект класса для поля ordering
print(w.Meta.ordering)  # обращение к полю ordering класса объекта w 
#>>> ['id']
print(w.__dict__)
#>>> {'user': 'root', 'passworld': '12345', 'meta': <__main__.Women.Meta object at 0x7eb00e9f9520>}
print(w.meta.__dict__) 
# >>> {'access': 'root@12345'}

# т.е. мы из класса Women можем создавать объекты класса Meta и обращаться к ним
# а из класса Meta так делать нельзя (единсвенное что можно прописывать в инициализаторе класса Meta например: self._t=Women.title и тогда обращение к атрибутам возможно, но этого не следует делать)
# т.е. следует придерживать правла внутренний класс не должен использовать внешний
