# Create a general class Animal
# ○ With a private attribute `name` set at initialization
# ○ With a method `get_name` that returns the animals name
# ● Create a class that inherits from the Animal class (see guide)
# ● Let the Cat class have:
# ○ A private variable `purr_sound` that is a string for the sound of the cat’s purring
# ○ A public method `purr` that prints out the `purr_sound`
# ● Show the initialization of a Cat object, print its name and make it purr.

class Animal:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.__purr_sound = "{} says mmmrrrrum".format(name)

    def purr(self):
        print(self.__purr_sound)


nnena = Cat("Nnena")
print(nnena.get_name())
nnena.purr()