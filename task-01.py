from abc import abstractmethod, ABC

class Vehicle (ABC):
  def __init__(self, make, model):
    self.make = make
    self.model = model

  @abstractmethod
  def start_engine(self):
    pass

class Car (Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")

class Motorcycle (Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model}: Мотор заведено")

class VehicleFactory (ABC):
  @abstractmethod
  def create_car(self, make, model):
    pass

  @abstractmethod
  def create_motorcycle(self, make, model):
    pass

class USVehicleFactory (VehicleFactory):
  def create_car(self, make, model):
    return Car(make, f'{model} (US Spec)')

  def create_motorcycle(self, make, model):
    return Motorcycle(make, f'{model} (US Spec)')

class EUVehicleFactory (VehicleFactory):
  def create_car(self, make, model):
    return Car(make, f'{model} (EU Spec)')
    
  def create_motorcycle(self, make, model):
    return Motorcycle(make, f'{model} (EU Spec)')

# Використання
vehicle1 = EUVehicleFactory().create_car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = USVehicleFactory().create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()
