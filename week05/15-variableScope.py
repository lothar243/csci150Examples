"""This program demonstrated the difference between a global scope and a local scope"""

def assign_value_local(newValue):
    myVariable = newValue
    
def assign_value_global(newValue):
    global myVariable
    myVariable = newValue

myVariable = 1
print(f"Before calling anything, {myVariable=}")
assign_value_local(2)
print(f"After calling assign_value_local, {myVariable=}")
assign_value_global(3)
print(f"After calling assign_value_global, {myVariable=}")