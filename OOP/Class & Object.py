class Parrot:
    #Class Attribute(Fields)
    species = "Bird"

    #instance attribute(Properties)
    def __init__(self, name, age):
        self.name = name
        self.age = age

#instantiate the Parrot class
blu = Parrot("Blue", 10)
woo = Parrot("Woo", 15)


#access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

#access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))
