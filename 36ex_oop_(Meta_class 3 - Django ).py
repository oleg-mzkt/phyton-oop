#36. Метаклассы в API ORM Django | Объектно-ориентированное программирование Python
# Можно использовать метаклассы для создания экземляров и связи их с соответсвующими атрибутами(полями) 
# например class Women(models.Model):
# атрибуты: 
#  title
#  content
#  photo
#  time_create  и др.
# т.е. при создании объекта w=Women(title='Ума Турман') , 
# автоматически будут созданы content, photo, time_create  и др.

# попробуем создать такой класс Women и вложенные метакласскласс Meta(type):
class Meta(type):
  def create_local_attrs(self, *args, **kwargs):
    for key, value in self.class_attrs.items():
      self.__dict__[key] = value
  
  def __init(cls, name, bases, attrs):
    cls.class_attrs = attrs
    cls.__init__ = Meta.create_local_attrs

class Women(models.Model):
    title = 'заголовок'
  content = 'контент'
  photo = 'путь к фото'

w = Wonen
print(w.__dict__)
