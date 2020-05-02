def reverse(string):
  L = []
  str = ""
  for i in string:
    str = i + str
  return str

string = input("Enter Name")
print(reverse(string))
