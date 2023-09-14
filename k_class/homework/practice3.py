class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        if self.is_running == False:
            self.is_running = True
            print("자동차가 출발합니다.")
        else:
            print("자동차가 이미 달리고 있습니다.")

    def stop(self):
        if self.is_running == True:
            self.is_running = False
            print("자동차가 멈췄습니다.")
        else:
            print("자동차가 이미 멈춰 있습니다.")

    def info(self):
        return print(f'브랜드: {self.brand} + 모델명: {self.model} + 연식{self.year}')

my_car = Car("Hyundae", "Avante", 2020)

my_car.info()
my_car.start()
my_car.stop()
my_car.start()
my_car.start()
my_car.stop()
my_car.stop()
