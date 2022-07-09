class Pirrot:
    #Instant attributes(Properties)
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #Instant methods
    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    def dance(self):
        return "{} is dancing".format(self.name)

#Initiate the object
blu = Pirrot("Blue", 10)

#Call the methods
print(blu.sing("Happy"))
print(blu.dance())
