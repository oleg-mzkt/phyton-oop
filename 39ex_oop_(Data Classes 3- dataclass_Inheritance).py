#39. Python Data Classes при наследовании | Объектно-ориентированное программирование Python

from dataclasses import dataclass, field, InitVar # подгружаем библиотеки с декоратором и функциями
from typing import Any

@dataclass
class Goods:
    current_uid = 0
    
    uid: int = field (init=False) 
    price: Any = None
    weight: Any = None
    
    def __post_init__(self):
        print("Goods: post_init")
        Goods.current_uid += 1
        self.uid = Goods.current_uid

# на основе класса Goods создадим класс Books:
@dataclass
class Books(Goods):
    title: str = "" 
    author: str = "" 
    price: float = 0
    weight: int | float = 0
    
b = Book(1,1000, 100, "Python ООП")
