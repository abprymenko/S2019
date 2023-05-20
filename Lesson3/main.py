from car import Car
from human import Human
humans = list()
car = Car("BMW x6")
daniil = Human("Daniil", True)
taras = Human("Taras")
dmytro = Human("Dmytro")
maria = Human("Maria")
humans.append(daniil)
humans.append(taras)
humans.append(dmytro)
humans.append(maria)
for human in humans:
    car.AddHumanToCar(human)
    car.ShowInfo(human)
