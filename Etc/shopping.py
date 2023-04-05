class Product:
    def __init__(self, name: str, price: int, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_price(self) -> int:
        return self.price * self.quantity

    def __str__(self):
        name_length = 0
        for char in self.name:
            if ord('가') <= ord(char) <= ord('힣'):  # 한글 문자인 경우
                name_length += 2
            else:
                name_length += 1

        # 한글과 영문의 폭을 고려하여 공백을 채워줍니다.
        padding = ' ' * (30 - name_length)

        info = f'{self.name}{padding}{self.quantity:>3}개 {self.get_price():>7}'
        return info


class ShoppingCart(Product):
    def __init__(self):
        self.shop_list = []

    def max_name_length(self) -> int:
        return max(len(product.name) for product in self.shop_list)

    def add(self, product) -> None:
        self.shop_list.append(product)

    def delete(self, product, quantity) -> None:
        if quantity == 0:
            self.shop_list.remove(product)
        else:
            return
    def total_price(self) -> int:
        return sum(product.get_price() for product in self.shop_list)

    def billing(self) -> str:
        for product in self.shop_list:
            print(product)

    def __str__(self):
        info = f'구매 품목:\n'
        for product in self.shop_list:
            info += f'{product}\n'
        return info
if __name__ == '__main__':
    p1 = Product('제주 삼다수 그린 2l', 1200, 5)
    p2 = Product('신라면(120g*5입)', 4100, 2)
    p3 = Product('CJ 햇반(210g*12입', 13980, 1)
    p4 = Product('몽쉘크림(12입)', 4780, 1)
    cart = ShoppingCart()
    cart.add(p1)
    cart.add(p2)
    cart.add(p3)
    cart.add(p4)
    print(cart)

    p4.quantity = 0
    cart.delete(p4, 0)
    p5 = Product('해태 구운감자(135g*5입)', 3580, 2)
    cart.add(p5)
    print(cart)

    get1 = p1.get_price()
    get2 = p2.get_price()
    get3 = p3.get_price()
    get5 = p5.get_price()

    print(f'구입 품목:')
    cart.billing()
    print('---------------------------------------')
    print(f'합계: {cart.total_price()}원')