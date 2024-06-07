from basket import *



class customer:
    couponBook = []
    
    def __init__(self, name):
        self.name = name
        self.cash = 0
        self.credit = 0
        self.coupon = ''
        


    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_cash(self):
        return self.cash
    
    def set_cash(self, cash):
        self.cash = cash

    def get_credit(self):
        return self.cash
    
    def set_credit(self, credit):
        self.credit = credit

    def get_coupon(self):
        return self.coupon
    
    def set_coupon(self, coupon):
        self.coupon = coupon

    def setBasket(self,basket):
        self.basket = basket

    def getBasket(self):
        return self.basket


Philip = customer("Phil")
Philip.set_cash(120000)
Philip.set_coupon("15%OFF")
Philip.set_credit(50000)
Philip.setBasket(basket1)
basket1.print_items()

#print(Philip.name, "Total Cash: $", Philip.cash,"\n","Total Credit: $", Philip.credit, "\n","Coupon Code: ", Philip.coupon)

#print(Philip.getBasket())