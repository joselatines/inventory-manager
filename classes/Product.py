class Product():
  def __init__(self, name, quantity, sell_price, buy_price):
    self.name = name
    self.quantity = quantity
    self.sell_price = sell_price
    self.buy_price = buy_price

  def __str__(self) -> str:
    return f'Product {self.name, self.quantity, self.buy_price, self.sell_price}'