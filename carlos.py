
# this is my first class called Home.
class Home:

    price_objs = 0.15

    def __init__(self, appliance, room, device, total_cost):
        self.appliance = appliance
        self.room = room
        self.device = device
        self.total_cost = total_cost

    def home_price(self):
        return '{} is debited from {}'.format(self.appliance, self.total_cost)

    def rate_of_price(self):
        return self.total_cost * Home.price_objs

    def under_rate(self):
        if self.total_cost <= 500:
            return True
        else:
            return "{} needs to be remove".format(self.appliance)



    @classmethod
    def home_rate(cls, amount):
        cls.price_objs = amount
Home.home_rate(0.18)
home1 = Home('sofa', 'bathroom', 'cell', 1000)
home2 = Home('table', 'bedroom', 'cam', 5000)
print(home1.rate_of_price())