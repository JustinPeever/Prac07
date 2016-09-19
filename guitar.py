

class Guitar:
    def __init__(self, name= '', year=0, cost=0):
        self.name = name
        self.cost = cost
        self.year = year

    def __str__(self):
        return"{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        age=2016-self.year
        return age
            #"the {} is 2016-{}={}".format(self.name, self.year, age)

    def is_vintage(self):
        return self.get_age() >= 50