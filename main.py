

""""
у каждой карты есть 4 параметра

а нет каждой у каждой карты есть 4 стороны
   xNorth =
   xEast =
   xSouth =
   XWest =

делается первый ход он определяет изначальное поле

потом

следующему игроку предоставляется выбор к какой карте
 и к какой стороне карты поставить свою карту

затем

мы сравниваем стороны и если где то они одинаковые
то игроки получают соответсвующие ресурсы +2



"""


class ToyClass:
    def instancemethod(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


x = 9
while x >= int(-5):
    print(x)
    x -= 1


