# TODO Airplane System with classes, inheritance, and overriding techniques
# Sleep method is used widely for demonstration
# Author: Team 8
# Usecase: Airlines system using Python3

from time import sleep


class Airplane:
    def __init__(self, Model_Number, rgsNo, capacity):
        self.modelNumber = Model_Number
        self.rgsNo = rgsNo
        self.capacity = capacity

    def printInfo(self):
        print("Model Number: ", self.modelNumber)
        sleep(1)
        print("Registration Number: ", self.rgsNo)
        sleep(1)
        print("Capacity: ", self.capacity)
        sleep(1)


class Flight(Airplane):
    def __init__(self, Model_Number, rgsNo, capacity, From, To, DepDate, DepTime, ArrDate, ArrTime):
        super().__init__(Model_Number, rgsNo, capacity)
        self.From = From
        self.To = To
        self.DepDate = DepDate
        self.DepTime = DepTime
        self.ArrDate = ArrDate
        self.ArrTime = ArrTime

    def printInfo(self):
        super().printInfo()
        print("Flying from: ", self.From)
        sleep(1)
        print("Flying To: ", self.To)
        sleep(1)
        print("DepDate: ", self.DepDate)
        sleep(1)
        print("DepTime: ", self.DepTime)
        sleep(1)
        print("ArrDate: ", self.ArrDate)
        sleep(1)
        print("ArrTime: ", self.ArrTime)
        sleep(1)


class Person:
    def __init__(self, FirstName, LastName, age):
        self.FirstName = FirstName
        self.LastName = LastName
        self.age = age

    def FullName(self):
        print(self.FirstName, self.LastName)


class Employee(Person):

    def __init__(self, FirstName, LastName, age):
        super().__init__(FirstName, LastName, age)

    def FullName(self):
        super().FullName()

    def isEmployee(self):
        return True


class Passenger(Person):

    def __init__(self, FirstName, LastName, age):
        super().__init__(FirstName, LastName, age)

    def FullName(self):
        super().FullName()

    def isPassenger(self):
        return True

    def flightRegistered(self, flight=None):
        self.bookedFlight = flight


def main():
    person = Person("Abdulmuhaymin", "Zakari", 26)
    employee = Employee("Roa", "Jamjom", 43)
    passenger = Passenger("Marcelock", "Tawabeer", 47)

    print("Person Instance: ")
    person.FullName()
    sleep(2)

    print("Employee Instance: ")
    employee.FullName()
    print("Is Employee? ", employee.isEmployee())

    sleep(2)

    print("Passenger Instance: ")
    passenger.FullName()
    print("Is Passenger? ", passenger.isPassenger())
    sleep(2)

    print("is Roa an employee? ", employee.isEmployee())
    print("Let's make a flight!")
    model = input("Enter the flight Model Number: ")
    rgsNo = input("Enter the Registration Number: ")
    Capacity = int(input("Capacity of the Flight: "))
    Flyingfrom = input("Flying from: ")
    FlyingTo = input("Flying To: ")
    DepDate = input("Departure Date: ")
    DepTime = input("DepTime ")
    ArrDate = input("ArrDate: ")
    ArrTime = input("ArrTime:  ")

    flight1 = Flight(model, rgsNo, Capacity, Flyingfrom, FlyingTo, DepDate, DepTime, ArrDate, ArrTime)

    # flight1 = Flight(765238, 2362567, 56, "Canada", "KSA", "2020, 5, 17", "10:30 pm",
    #                  "2020, 5, 17", "10:32 am")

    print("Flight initialized with the following properties: ")
    sleep(1)
    flight1.printInfo()
    ans = input("You want to book this flight for The passenger '" + passenger.FirstName + "'? (y/n) ")
    if (ans == 'y') or (ans == 'Y'):
        flight1.capacity = flight1.capacity - 1;
        passenger.bookedFlight = flight1.modelNumber
        print("Success! you are registered for the Flight: ", flight1.modelNumber, " on ", flight1.DepDate)
        sleep(1)
        print("Flight Capacity is now ", flight1.capacity)
    else:
        print("OK")


if __name__ == '__main__':
    main()
