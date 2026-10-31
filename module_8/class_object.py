class phone:
    category = "electronics" #class attribute

    #instance attribute
    def __init__(self,model,battery,camera,battery_percentage=100):
        self.model= model
        self.battery = battery
        self.camera = camera
        self.battery_percentage = battery_percentage

    #methods
    def charge(self,hour):
        self.battery+= hour
        print(f"charge completed by {hour}")

    def capture(self,photo):
        if(self.battery_percentage)<=0:
            print("no charge")

        else:
            self.battery_percentage -= photo
            print(f"photo captured in {self.model}")

Iphone = phone("Iphone17",5700,108)
print(type(Iphone))
Iphone.category = "super electronics"
print(vars(Iphone))
print(Iphone.battery_percentage)
Iphone.capture(10)
print(Iphone.battery_percentage)
