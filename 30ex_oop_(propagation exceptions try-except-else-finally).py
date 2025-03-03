#30. Распространение исключений (propagation exceptions) | ООП Python
# try-except-else-finally

#########1#########
print("text1")
print("text2")
print("text3")

def func1():
  return 1/0

print("text4")
print("text5")
print("text6")
print("text7")

#func1() # если закоментировать - ошибка не возникнет т.к. нет вызова ф-ции func1():
#>>> Traceback (most recent call last):
#>>>  File "<main.py>", line 17, in <module>
#>>>  File "<main.py>", line 10, in func1
#>>> ZeroDivisionError: division by zero
#  Исключение отображается в двух строчках  line 10, line 17 т.е. возниклов 17-ой и расспространилось до уровня main где мы его не обрабатываели т.е. в 10-ой строке
# при появлении исключения  print("text8") уже не вызвывается

#########2#########

def func2():
    return 1/0
def func3():
    return func2()

func3()
#>>> Traceback (most recent call last):
#>>>   File "<main.py>", line 32, in <module>
#>>>   File "<main.py>", line 30, in func3
#>>>   File "<main.py>", line 28, in func2
# ZeroDivisionError: division by zero
#   Стек распространения ошибки несколько другой: line 32  → line 30→ →line 28: ZeroDivisionError

print("text8")
print("text9")
