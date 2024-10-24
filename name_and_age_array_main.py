#initialize functions
#function that checks if the name is valid
#the function returns an error message if the name is invalid
def valid_name(name):
    


#function that checks if the age is valid
#the function returns an error message if the age is invalid
def valid_age(age):
    try:
        age = int(age)
        return age <= 1 and age <= 100
    except:
        print("Invalid input")

#funnction that asks the user to input a valid name and age
def user_input():

    while True:
        try:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
        except:
            print("Invalid input")
            

        
    


#call the functions
#display the output