#30. Распространение исключений (propagation exceptions try-except-else-finally) | ООП Python
# 1
#
#########1#########
print("text1")
print("text2")
print("text3")

def func1():
  return 1/0 #  1 делить на 0 нельзя поэтому будет ОШИБКА!!!

print("text4")
print("text5")
print("text6")
print("text7")

#func1() # если закомментировать - ошибка не возникнет т.к. нет вызова ф-ции func1():
#>>> Traceback (most recent call last):
#>>>  File "<main.py>", line 17, in <module>   # 2) ОШИБКА РАССПРОСТРОНЯЕКТСЯ ДО САМОЙ ФУНКЦИИ
#>>>  File "<main.py>", line 10, in func1      # 1) ОШИБКА ВОЗНИКАЕТ НЕПОСРЕДСТВЕННО ПРИ ВЫЗОВЕ ФУНКЦИИ
#>>> ZeroDivisionError: division by zero
#  Исключение отображается в двух строчках  line 10, line 17 т.е. возникло 17-ой и распространилось до уровня main,
# где мы его не обрабатываели т.е. в 10-ой строке (при появлении исключения  остальной код не вызывается print("text8"))

#########2#########
# Ст
def func2():
    # try:
        return 1/0
    # except:
    #     print("func2 - Error: - обработка искл. произошла на уровне MAIN")
    #     print(" на более нижникх уровнях обработка не происходит даже если есть блок try: except:")
def func3():
    # try:
        return func2()
    # except:
    #     print("func3-Error: -на уровнях ниже т.е. при вызове функции func3 обработка исключений не происходит")
# отлавливать можно даже при самом вызове функции, если обработка исклдючений не настроена на более высоком уровне)
try:
    func3()
except:
    print("Error - вызов функции невозможен")
#>>>Traceback (most recent call last):
#>>>File "<main.py>", line 32, in <module># 1) через try-except обрабатывать исключения  можно на любом уровне (если main - остальные не будут обрабатываться)
#>>>File "<main.py>", line 30, in func3   # 2) на уровне func3 - тогда на уровне func2 не будет обрабатываться3
#>>>File "<main.py>", line 28, in func2   # 3) либо на самом месте вызова функции с её конкретными параметрами - возможно недопустимыми
# ZeroDivisionError: division by zero
#   Стек распространения ошибки несколько другой: line 32  → line 30→ →line 28: ZeroDivisionError

print("text8")
print("В критических функциях достаточно генерировать исключения - а их обработку выполнять на более глобальных уровнях")
print("Например класс для печати данных с принтера:")
print("class PrintData()")
print("def print_connection(self):\ndef senf_data(self):\ndef no_sheets(self):")
print("тогда все ошибки связанные с принтером можно обрабатывать на верхнем глобально уровне: PrintData():")
print("а нижние уровни:\nнет соединения:\n нет бумаги:\n и т.д. ...\n-только сигнализируют о проблемах")