class Camera:
    def __init__(self,name):
        self.name = name

    def capture(self):
        print(f"Photo is captured")

class Phone(Camera):
    def __init__(self, name,resolution):
        super().__init__(name)
        self.resolution = resolution

    #method overriding
    def capture(self):
        print(f"Photo is captured by {self.name}")

class DSLR(Camera):
    def __init__(self, name,resolution):
        super().__init__(name)
        self.resolution = resolution
    
    #method overriding
    def capture(self):
        print(f"Photo is captured by {self.name}")

class Drone(Camera):
    def __init__(self, name,resolution):
        super().__init__(name)
        self.resolution = resolution
    
    #method overriding
    def capture(self):
        print(f"Photo is captured by {self.name}")

phone = Phone("Nokia",50)
# print(vars(phone))
dslr = DSLR("DSLR",200)
drone = Drone("Drone",150)

phone.capture()
dslr.capture()
drone.capture()