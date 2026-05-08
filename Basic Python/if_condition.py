#use of if condition
year_of_birth= int (input("enter your year of birth :"))
#getting input from user 
currnt_year = 2025
#current year
age = currnt_year - year_of_birth
#age calculation
if age< 18:
    #if condition to check age
    print('your age is',age, 'you are minor so you are not allow to watch movie ')
else:
    #else condition if age is above 18
    print("your age is",age,"you are above 18 allow to watch movie")    
    

