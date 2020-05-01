"""
    Resource: 4 Pillar Udemy
    Class and Object Example with changing the name problem
"""
class Employee:
    name = "Akshay"
    def changeNames(self):
        Employee.name = "Omkar"

employee = Employee()
#Previous Name
print(employee.name)
employee.changeNames()
#Changed Name
print(employee.name)