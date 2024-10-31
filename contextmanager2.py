# КОНТЕКСТНЫЙ МЕНЕДЖЕР вариант 2
# https://www.youtube.com/watch?v=IG6oIbuSwCc
# - это способ высвободить ресурсы автоматически, если файл забыли закрыть (не только с файлами)
#Контекстный менеджер это удобный способ инкапсулировать логику работы с каким то ресурсом
#try-except-finally, в том числе гарантировать освобождение ресурса, его закрытие. Например 
#try-except-finally, в том числе гарантировать освобождение ресурса, его закрытие. Например 
#имеют менеджеры контекста, например для работы с файлами.
#если пишем менеджер через contextlib то используем yield возвращающий ровно 1 значение (наш ресурс)

from contextlib import contextmanager
class Resource:
    def __init__(self):
        self.opened = False
        
    def open(self,*args):
        print(f'Resource was opened with arguments {args}.')
        self.opened = True
    
    def close(self):
        print('Resource was closed!')
        self.opened = False
        
    def __del__(self):
        if self.opened:
            print(f'Memory leak detected! \nResource was not normaly closed!')
    
    def action(self):
        print('Do something with resource...')
#@contextmanager    
#def open_resource(*args):
#    resource = None
#    try:
#        resource = Resource()
#        resource.open(args)
#        yield resource
#    except:
#        raise 
#    finally:
#        if resource:
#            resource.close()
#
class ResourceWorker:
    def __init__(self,*args):
        self.args = args
        self.resource = None
    def __enter__(self):
        self.resource = Resource()
        self.resource.open(*self.args)
        return self.resource
    def __exit__(self,exc_type,exc_val,exc_tb): # exc_type - тип исключение ,exc_val - его значение ,exc_tb - его Traceback(трасировка)
    # - если все эти исключения None - значит ничего не упало не сломалось
        if self.resource:
            self.resource.close()

if __name__ == '__main__':
    with ResourceWorker(1,2,3) as res:
        res.action()
        raise ValueError('Stop error') # пайтон позволяет использовать для логики с исключениями(ошибками) гарантированным высвобождением памяти после исключений
