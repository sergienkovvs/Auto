from time import sleep

from main import Auto


class Truck(Auto):
    max_load = 0

    def __init__(self, brand, age, mark, max_load):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    def load(self):
        sleep(1)
        print("load")
        sleep(1)

    def write(self):
        print(self.brand, self.age, self.mark, self.max_load)


if __name__ == "__main__":
    car1 = Truck("", 0, "", 0)
    car1.load()
    car1.move()
    car1.brand = "ford"
    car1.age = 3
    car1.mark = "f-150"
    car1.max_load = 1200
    car1.write()

    car2 = Truck("", 0, "", 0)
    car2.load()
    car2.move()
    car2.brand = "MAN"
    car2.age = 5
    car2.mark = "TGX"
    car2.max_load = 100.000
    car2.write()