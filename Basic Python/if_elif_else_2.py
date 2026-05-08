# To find the grade of the student based on the marks 0 - 100 .
marks = int(input("Enter the marks of the student :"))
# Take input from user .
if marks >= 0 and marks <=100: 
    # Check if the marks is in range of 0 to 100 or not.
    if marks >= 90:
      #check marks is greater than 90.
      print( "A")
    elif marks >=80:
     # check marks is greater than 80.
      print("B")
    elif marks >= 70:
      #check marks is greater than 70.
      print("C")
    elif marks >= 60:
      #check marks is greater than 60 .
      print("D")
    else :
      # if marks is less than 60 .
      print("E")
else:
    print("Invalid Input")
