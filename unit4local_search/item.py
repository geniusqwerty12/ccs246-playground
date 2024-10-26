class Item:
    def __init__(self, name, price):
      self.name = name
      self.price = price

    def __str__(self):
       return "{}:{}".format(self.name, self.price)