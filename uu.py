class Shirt:
    def __init__(self,shirt_color,shirt_price,shirt_size):
        self.color = shirt_color
        self._price = shirt_price
        self.size = shirt_size
    def set_price(self,new_price):
        self._price = new_price
