class Product:
    discount_rate:float = 0.0
    def __init__(self, name:str, price:int, quantity:int):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def name(self) :
        return self.__name

    @property
    def price(self) :
        sales_price = int(self.__price*(1-Product.discount_rate))
        return sales_price

    @property
    def quantity(self) :
        return self.__quantity

    @quantity.setter
    def quantity (self, quantity):
        self.__quantity = quantity

    def get_price(self):
        return int(self.__price * (1-Product.discount_rate) * self.__quantity)

    def __str__(self):
        return f'{self.__name:30s}\t{self.__price:>6,d}원{self.__quantity:3d}개'
    @classmethod
    def change_rate(cls,rate:float):
        Product.discount_rate=rate

class ShoppingCart:
    def __init__(self):
        self.__shop_List = []

    def add(self,pdt):
        self.__shop_List.append(pdt)

    def delete(self,pdt,qty):
        updated = False
        for p in self.__shop_List:
            if p.name == pdt.name:
                p.quantity -= qty
                updated = True
                if p.quantity <= 0:
                    self.__shop_List.remove(p)
                break
        return updated

    def total_price(self):
        sum=0
        for p in self.__shop_List:
            sum += p.get_price()

        return sum

    def billing(self):
        print('구입 품목:\n')

        for p in self.__shop_List:
            print(f'{p.name:30s}\t{p.quantity:3d}개\t{p.price*p.quantity:6,d}')
        print(f'{58*"-"}')
        print(f'{"합계":45s}{self.total_price():6,d} ')

    def __str__(self):
        shop = ''
        for p in self.__shop_List:
            shop += f'{p}]\n'

        return shop

if __name__ == '__main__':
    products = [Product('제주 삼다수 그린 2L', 1200, 5),
                Product('신라면(120g*5입)', 4100, 2),
                Product('CJ 햇반(210g*12입)', 13980, 1),
                Product('몽쉘크림(12입)', 4780, 1)]

    my_cart = ShoppingCart()

    for p in products:
        my_cart.add(p)


    my_cart.delete(products[3], 1) #구매 취소

    my_cart.add(Product('해태 구운 감자(135g*5입)', 3580, 2)) #제품 추가

    Product.change_rate(0.1)
    my_cart.billing()