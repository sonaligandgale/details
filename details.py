import sys

if len(sys.argv) == 3:
  script_name = sys.argv[0]
  name = sys.argv[1]
  rollno = sys.argv[2]
  print("User provided input values:")
else:
  script_name = sys.argv[0]
  name = "Riya"
  rollno = "101"
  print("No input given - using default values:")


print("script name: ", script_name)
print("name: ", name)
print("roll no: ", rollno)
