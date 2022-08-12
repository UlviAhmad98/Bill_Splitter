class Mammal:
    def __init__(self):
        self.bio_class = "mammal"

    def greet(self):
        print("I am a {}!".format(self.bio_class))


class Dolphin(Mammal):
    def greet(self, name="dolphin"):
        super().greet()
        print(f"I am a {name}!")
# create class Dolphin here