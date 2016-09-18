

class ProgrammingLanguage:
    def __init__(self, name= '', typing='', reflection='', year=''):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def _str_(self):
        print("{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year))


    def is_dynamic(self):
        print("Typing = {},".format(self.typing))