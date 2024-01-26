class Employee:
    employee_count = 0

    def _init_(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.employee_count += 1

    def average_salary(self):
        # Implement your logic for average salary calculation here
        pass

class FulltimeEmployee(Employee):
    def _init_(self, name, family, salary, department):
        super()._init_(name, family, salary, department)

# Creating instances of both classes
employee1 = Employee("John Doe", "Family Doe", 50000, "HR")
fulltime_employee1 = FulltimeEmployee("Jane Doe", "Family Doe", 60000, "IT")

# Calling member functions
employee1.average_salary()
fulltime_employee1.average_salary()