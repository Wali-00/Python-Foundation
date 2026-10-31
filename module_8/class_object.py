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


#inheritance

#child/derived class
class Smartphone(phone):
    def __init__(self, model, battery, camera, processor):
        super().__init__(model, battery, camera)
        self.processor = processor

    def charge(self, hour):
        print("First charging is process")
        super().charge(hour)

pro = Smartphone("Iphone18",57000,108,"A26")
print(pro.processor)
pro.charge(10)

class Cooling_Mechanism:
    def __init__(self,cooling_mode):
        self.cooling_mode = cooling_mode

    def cooling_on(self):
        print(f"system is begin cooling by {self.cooling_mode}")

class Smartphone_coolingMode(Smartphone,Cooling_Mechanism):
    def __init__(self, model, battery, camera, processor,cooling_mode):
        Smartphone.__init__(self,model, battery, camera, processor)
        Cooling_Mechanism.__init__(self,cooling_mode)

pro_cooling = Smartphone_coolingMode("Black Shark",6000,108,"Snapdragon","Nitrogen")
print(vars(pro_cooling))