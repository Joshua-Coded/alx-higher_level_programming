class Object :
    one = "first"
    two = "second"
    three = "third"


    def __init__(self, attr):
        self.attr = attr

    def lookup(self):
        print(self.one, self.two, self.three, self.attr)

n = Object(2)
n.lookup()


# passing both the objects
# and the class as argument
