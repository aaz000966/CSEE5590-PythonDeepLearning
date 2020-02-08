class Employee:
    totalInstances = 0
    avgSalary = []

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.totalInstances += 1
        Employee.avgSalary.append(salary)

    def getInfo(self):
        print(self.name,
              self.family,
              self.salary,
              self.department)


class FullTimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        self.fullTime = True
        Employee.__init__(self, name, family, salary, department)

    def getInfo(self):
        print(self.name,
              self.family,
              self.salary,
              self.department,
              "fulltime?", self.fullTime)


def avg(lst):
    return sum(lst) / len(lst)


def main():
    Employee1 = Employee("Zakari", "Abdu", 132000, "CS")
    Employee1.getInfo()
    Employee2 = FullTimeEmployee("Marya", "Solar", 96000, "IT")
    Employee2.getInfo()
    print(Employee2.__class__.totalInstances)
    print(int(avg(Employee.avgSalary)))


if __name__ == "__main__":
    main()

# 1. Create a class Employee and then do the following
# a. Create a data member to count the number of Employees
# b. Create a constructor to initialize name, family, salary, department
# c. Create a function to average salary
# d. Create a Fulltime Employee class and it should inherit the properties of Employee class
# e. Create the instances of Fulltime Employee class and Employee class and call their member functions.
