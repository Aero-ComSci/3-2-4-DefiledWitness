loop = False
def assignment1():
    print("Assignment 1 Completed.")

def assignment2():
    print("Assignment 2 Completed.")

assignment1()
assignment2_result = assignment2()
print("\n Next Step: \n")
def execute_assignment(assignment_number):
    if assignment_number == "1":
        assignment1()
    if assignment_number == "2":
        assignment2()
while loop == False:
    Number = input("Assignment number 1 or 2? Or would you like to quit?: \n").lower()
    if Number == "quit":
        loop = True
    else:
        execute_assignment(Number)
