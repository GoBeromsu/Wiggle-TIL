class Product:
    rate: float = 0.0

    def __init__(self, name: str, price: int, quantity: int):
        self._name = name
        self._price = price
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    def get_price(self):
        return int(self._price * (1 - Product.rate) * self._quantity)

    def __str__(self):
        return f'{self._name:35s}\t{self._price:>7,d}\t{self._quantity:3d}'

    @classmethod
    def get_discount_rate(cls):
        return cls.rate

    @classmethod
    def set_discount_rate(cls, rate):
        cls.rate = rate


class Sales_Product(Product):
    rate: float = 0.2

    def __init__(self, name: str, price: int, quantity: int):
        super().__init__(name, price, quantity)

    def get_price(self):
        return int(self._price * (1 - Sales_Product.rate) * self._quantity)


class Clearance_Product(Product):
    rate: float = 0.5

    def __init__(self, name: str, price: int, quantity: int):
        super().__init__(name, price, quantity)

    def get_price(self):
        return int(self._price * (1 - Clearance_Product.rate) * self._quantity)
class ShoppingCart:
    def __init__(self):
        self._shop_List = []

    def add(self, pdt):
        self._shop_List.append(pdt)

    def delete(self, pdt, qty):
        updated = False
        for p in self._shop_List:
            if p.name == pdt.name:
                p.quantity -= qty
                updated = True
                if p.quantity <= 0:
                    self._shop_List.remove(p)
                break
        return updated

    def total_price(self):
        sum = 0
        for p in self._shop_List:
            sum += p.get_price()

        return sum

    def billing(self):
        print('구입 품목:\n')
        print(f'{"품목명":<35s}{"수량":>3}{"정상가":>7} {"할인가":>7}')
        shop = ''
        for p in self._shop_List:
            name_length = 0
            for char in p._name:
                if ord('가') <= ord(char) <= ord('힣'):  # 한글 문자인 경우
                    name_length += 2
                else:
                    name_length += 1

            # 한글과 영문의 폭을 고려하여 공백을 채워줍니다.
            padding = ' ' * (35 - name_length)
            shop += f'{p._name}{padding}\t{p.price:>7,d}\t{p.quantity:5d}\t{p.get_price():>6,d}\n'
        print(shop)
        print(f'{70 * "-"}')
        print(f'{"합계":<50}{self.total_price():>10,} ')

    def __str__(self):
        shop = ''
        for p in self._shop_List:
            shop += f'{p}\n'

        return shop

if __name__ == '__main__':
    products = [Product('제주 삼다수 그린 2L', 1200, 5),
                Product('신라면(120g*5입)', 4100, 2),
                Sales_Product('CJ 햇반(210g*12입)', 13980, 1),
                Clearance_Product('노스페이스 올라운드 폴로 NT7PN00B', 65000, 1)]

    my_cart = ShoppingCart()

    for p in products:
        my_cart.add(p)

    my_cart.billing()
