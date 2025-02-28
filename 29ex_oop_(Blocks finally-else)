#29. Обработка исключений. Блоки else и finally | Объектно-ориентированное программирование Python
# 0) ValueError as z: переменная 'z' может быть использована для вывода исключения через print(z) 
# 1) else: - выполняется если не произошло никаких ИСКЛЮЧЕНИЙ
# 2) finally: - выполняется в любом случае
# 3) практический пример конструкции 
# 4) with open ("myfile.txt") as f: - конструкция позволяет автоматически закрывать файл и блок finally уже не обязателен
# 5) блок finally для обработки исключений некоторой ф-ции

# try:
#     x, y = map(int, input().split())
#     res = x / y 
# except ZeroDivisionError as z: # -переменная типа 'z' будет являтся ссылкой на экземпляр класса исключения
#     print(z) # ссылка 'z' может быть использована для вывода исключения

# except ValueError as z:
#     print(z)
    
# ############## 1 ##############
# else:
#     print('Блок else - исключений не произошло')

# ############## 2 ##############
# finally:
#     print('Блок finally выполняется всегда')
    
# ############## 3 ##############

try:
    f=open("myfile.txt")    #   файл открытый для чтения
    f.write("hello")        #   попытка записи файла - Другая ошибка
except FileNotFoundError as z:
    print(z)
except:
    print('Другая ошибка')
# по программе файл оставлся открытым
# любой файл нужно закрывать даже при возникновении ошибок
finally:
    # if f:
    #     f.close()
    print('Файл закрыт')
# ############## 4 ##############
try:
   with open ("myfile.txt") as f:
       f.write("hello")
except FileNotFoundError as z:
    print(z)
except:
    print('Другая ошибка')
# блок finally lдля закрытия файла уже не обязателен

# ############## 5 ##############
print('пример 5 обработки исключения недопустимых значений ф-ции')

def div(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Деление на ноль')
res = 0 

try:
    x, y = map (int, input().split())
    res = div(x, y)
except ValueError as z:
    print(z)
except:
    print('Другая ошибка')
finally:
    print('finally выполняется до retun')

print(res) # вызво оператора return происходит в последнюю очередь
