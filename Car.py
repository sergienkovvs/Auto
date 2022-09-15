from main import Auto


class Car(Auto):
    max_speed = 0

    def __init__(self, brand,age, mark, max_speed):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print("max_speed " + str(self.max_speed))

if __name__ == "__main__":
    car3 = Car("kia", 18, "rio", 180)
    car3.move()

    car4 = Car("WV", 17, "Golf", 190)
    car4.move()