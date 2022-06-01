from classcar import Car
from classEcar import ElectricCar


my_car = Car('fiat', 'argo', 2018)
print(my_car.descriptive_name())
my_car.update_odometer(23050)
my_car.read_odometer()
my_car.increment_odometer(500)
my_car.read_odometer()


my_ecar = ElectricCar('tesla', 'model s', 2016)
print(my_ecar.descriptive_name())
my_ecar.battery.describe_battery()
my_ecar.battery.get_range()
