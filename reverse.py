def reverse(string):
  str = ""
  for i in string:
    str = i + str
  return str

string = input("Enter Name")
print(reverse(string))

# other method to reverse string
print(string[::-1])
