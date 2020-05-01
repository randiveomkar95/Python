"""
    Resource: 4 Pillar Udemy
    Class and Object Example with changing the name problem
"""
class Employee:
    name = "Akshay"
    def changeNames(self):
        Employee.name = "Omkar"

employee = Employee()
print(employee.name)
employee.changeNames()
print(employee.name)