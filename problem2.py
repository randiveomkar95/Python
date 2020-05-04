"""
Write a Python program which accepts a sequence of comma-separated numbers from user and
generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :  List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

userinput = input("Enter comma separated numbers ")
print("User input numbers are : " + userinput)

numbers = userinput.split (",")

List = list(numbers)
tuple = tuple(numbers)

print("List: " , List)
print("Tuple: " , tuple)
