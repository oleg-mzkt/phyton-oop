#31. Инструкция raise и пользовательские исключения | ООП Python
# 1) Мы можем генерировать исключения с помощью комманды raise

######## 1 ########

print("Test1")
print("Test2")
print("Test3")
#1/0                    #>>> ZeroDivisionError 
raise ZeroDivisionError #>>> ZeroDivisionError 
print("Test4")
print("Test5")
print("Test6")
