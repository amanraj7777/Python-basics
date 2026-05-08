#Create a Python script that prints numbers from 10 to 1 using a while loop.


# x  = 10
# while x > 0:
#     print(x)
#     x -= 1


#- Write a program that keeps taking user input until the user enters “exit” using a while loop.


while True:
    user_input = input("Enter something (type 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("Exiting the program...")
        break
    else:
        print(f"You entered: {user_input}")




       