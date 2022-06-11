class Phone:
  def __init__(self,os,name):
    self.os=os
    self.name=name

class Price:
  def __init__(self,money):
    self.money=money

class whatscall(Phone, Price):
  def __init__(self,os,name,money):
    Price.__init__(self,money)
    Phone.__init__(self, os, name)

  def show_name(self):
      print(f"{self.os} {self.name} {self.money}")
mycall = whatscall('ios', 'iphone12', '1,250,000')
mycall.show_name()

# 다중 상속에서는 부모 클래스를 부르려면 명시적으로 불러야해
# 그래서 위에서 부모 클래스의 생성자를 whatscall에서 실행 시킨거야
# 사실 이미 상속을 받았으니 다르게 해도 되긴함// 동규 원래 코드라던가
# 아 그리고 init의 경우 파이썬 생성자로 인식하는게 __init__인거 같던데?
# 물론 init() 이렇게 써도 되는데 이렇게 쓰려면, Object.init() 이렇게 불러줘야할거야
# 에러 뜬 원인 중에 이거도 한 몫 했을 듯

# Error 1
# TypeError: init() takes 3 positional arguments but 4 were given
# class whatscall(Phone, Price):
#   def init(self,os,name,money):
#     super().init(os,name,money)
# 다중 상속에서 super로 바로 생성자를 부르면, 파이썬의 경우 첫 번째 객체인 Phone을 인식할거 
# 언어에 따라 다중 상속 상황에서 조금씩 다를거고
# 결론은 부모 클래스의 생성자 형식에 맞지 않게 값을 많이 입력해서 그렇다!
