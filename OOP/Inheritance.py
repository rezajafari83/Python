#Parrent Class
class Bird:
    def __init__(self):
        print("Bird is ready!")
    
    #Instant methods
    def Whoisthis(self):
        print("Bird")
    def Swim(self):
        print("Swim faster")

#Child Class
class Pinguin(Bird):
    def __init__(self):
        #Call super function
        super().__init__()
        print("Pinguin is ready!")

    def Whoisthis(self):
        print("Pinguin")

    def Run(self):
        print("Run faster")

Peggy = Pinguin()
#Child class edits this method of parrent class
Peggy.Whoisthis()
#Child class inherits this method from parrent class
Peggy.Swim()
#Methods of Child class are extended by this new method
Peggy.Run()