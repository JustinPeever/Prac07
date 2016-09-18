

class Guitar:
    def __init__(self, name= '', year=0, cost=0):
        self.name = name
        self.cost = cost
        self.year = year

    def _str_(self):
        print("{} ({}) : ${}".format(self.name, self.year, self.cost))

    def get_age(self):
        age=2016-self.year
        print("the {} is 2016-{}={}".format(self.name, self.year, age))

    def is_vintage(self):
        if (2016-self.year) >= 50:
            print("True")
        else:
            print("False")

