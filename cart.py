from items import *

class cart:
    def __init__(self, items, total):
        self.items = items
        self.total = total
        self.basket = []

    def __str__(self):
            return f"{self.items} {self.total}"
    


    def add_items(items,basket,qty):
         i = 0
         while i < qty:
              basket.append(items)

    

    
    
    basket1 = []
    poptart = ("poptart", 3425324, 1.50)

    add_items(poptart,basket1, 5)
    



    
              
