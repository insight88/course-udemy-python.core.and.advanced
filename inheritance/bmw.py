from abc import abstractmethod, ABC


class BMW(ABC):
    # ! ABC : Abstract Base Class, 이 클래스를 상속하는 모든 클래스는 base class의 method를 강제적으로 override 해야함

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    # ! 추상화시킬 method에 @abstractmethod 데코레이터를 선언하고 pass
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass


class ThreeSeries(BMW):
    # * class의 parameter로 parent class name을 전달하면 상속

    def __init__(self, cruiseControlEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):
        print(self.cruiseControlEnabled)

    def start(self):
        super().start()
        print("Button Start")

    def stop(self):
        super().stop()
        print("Button stop")

    def drive(self):
        print("Three Series is being driven")


class FiveSeries(BMW):

    def __init__(self, parkingAssistEnabled, make, model, year):
        super().__init__(make, model, year)
        # ! super()로 parent calss를 호출하면 parameter로 self를 전달하지 않아도 됨
        self.parkingAssistEnabled = parkingAssistEnabled

    def start(self):
        super().start()
        print("Remote Start")

    def stop(self):
        super().stop()
        print("Remote stop")

    def drive(self):
        print("Five Series is being driven")


bmw = ThreeSeries(True, "BMW", "328i", "2018")
print(bmw.cruiseControlEnabled)
print(bmw.make)
print(bmw.model)
print(bmw.year)

bmw.start()
bmw.stop()
bmw.display()

bmw = FiveSeries(True, "BMW", "328i", "2018")
print(bmw.parkingAssistEnabled)
print(bmw.make)
print(bmw.model)
print(bmw.year)

bmw.start()
bmw.stop()
bmw.drive()
