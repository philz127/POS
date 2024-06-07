from items import *


class basket:
    def __init__(self):  
        self.basket = self
        self.space = []
        self.total = 0
        self.discount = 0
      
    def set_capacity(self):
        self.capacity = len(self.space)

    def add_items(self, items, qty):
        x = 0
        while x < qty:
            self.space.append(items)
            x= x+1
        self.get_total()

    def rmv_items(self, items, qty):
        x = 0
        while x < qty:
            self.space.remove(items)
            x= x+1
        self.get_total()
     
    def get_total(self):
        x= 0
        y= len(self.space)
        curr_total = 0
        while x < y:
            curr_total = round(curr_total,2) + self.space[x].get_price()
            x=x+1
        self.total = curr_total
        
        return print("Total: $", round(self.total,2))
    
    def apply_coupon(self, coupons):
        coupons.apply_dscnt(self)  
        
    def print_items(self):
        x = 0
        y = len(self.space)
        while x < y:
            print(self.space[x], sep="  ")
            x = x+1
        self.set_capacity()

    



basket1 = basket()



cookies = items("cookies", 32423, 1.46)
poptarts = items("poptarts", 93842, 1.65)
rice = items("rice", 3287423, 3.00)
slim_jim = items("slim jim", 329873, .46)


#basket1.add_items(rice, 44)
#basket1.rmv_items(rice,13)
#basket1.print_items()
#basket1.get_total()
#print(basket1.total,"Total Item Count:", basket1.capacity, sep = "  ")


#ten_percent = coupons("10% OFF")
#twnty_percent = coupons("20% OFF")
#thrty_percent = coupons("30% OFF")
#frty_percent = coupons("40% OFF")
#dollar = coupons("$1 OFF")
#five_dollar = coupons("$5 OFF")
#ten_dollar = coupons("$10 OFF")
#twenty_dollar = coupons("$20 OFF")

#print("\n\n")
#basket1.apply_coupon(twnty_percent)
















    








        
   
    
    
    