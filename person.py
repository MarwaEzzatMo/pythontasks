


class Person:

    def __init__(self, full_name, money, sleepmood, healthRate):
        self.full_name = full_name
        self.money = money
        self.sleepmood = sleepmood
        if healthRate > 0 and healthRate < 100:
            self.healthRate = healthRate

    def sleep(self, hours):
        if hours == 7:
            self.sleepmood = "happy"
        elif hours > 7:
            self.sleepmood = "Lazy"
        else:
            self.sleepmood = "tired"

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate == 50

    def buy(self, *items):
        for item in items:
            self.money -= 10

