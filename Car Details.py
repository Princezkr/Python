class car:
    def __init__(self,make,model,mileage,colour,year,price):
        self.make=make
        self.model=model
        self.mileage=mileage
        self.colour=colour
        self.year=year
        self.price=price
    def display_details(self):
        print("Car Details")
        print("Make: ",self.make)
        print("Model: ",self.model)
        print("Mileage: ",self.mileage)
        print("Colour: ",self.colour)
        print("Year: ",self.year)
        print("Price: ",self.price)
    def start(self):
        print(f"{self.make} {self.model} Is Starting")
    def stop(self):
        print(f"{self.make} {self.model} Is Stopped")
    def Update(self,Value):
        self.price=Value

car1=car("Toyota","Fourtuner",18,"Black",2024,200000)
car2=car("Tata","Nexon",19,"White",2025,500000)

print(car1.display_details())
car1.Update(600000)
print(car1.display_details())
print(car2.display_details())
car2.Update(700000)
print(car2.display_details())
