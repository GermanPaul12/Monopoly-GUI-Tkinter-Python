class Player:
    def __init__(self, money=1500, ground=0, real_estate=0, money_per_round=200, tax_estate=0.2, tax_ground=0.1):
        self.money = money
        self.ground = ground
        self.real_estate = real_estate
        self.money_per_round = money_per_round
        self.tax_estate = tax_estate
        self.tax_ground = tax_ground
        
        
        
    def calc_tax(self):    
        self.money += self.money_per_round - self.ground * self.tax_ground - self.real_estate * self.tax_estate
        return self.money
