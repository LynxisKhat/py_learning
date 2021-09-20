class Car():

    strwheel = 1 #class level attribute

    def __init__(self,name,wheels):
        self.name = name
        self.wheels = wheels

    def drive(self):
        print(f"{self.name} has {self.wheels} wheels that is driving")
    
    #class level method
    @classmethod
    def common(cls):  
        print(f'All car have {cls.strwheel}steeringwheel .')

#car1 = Car("Mercedes","4")
#car1.drive()
#Car.common()
#print(Car.strwheel)

#class level attribute and method can call without creating object