

class items:
    def __init__(self, name, sku, price):
        self.name = name
        self.sku = sku
        self.price = price

    def __str__(self):
            return f"{self.name} {self.sku} {self.price}"
    
    def get_price(self):
        return (self.price)
         
         
    def set_price(self,x):
         self.price = x
    

    
  
cake = items("cake", 245239, 1.65)






    