#initialize the array
name = []
age = []

#loop that prompts the user for input
while True:
    #Loop that retries when a user enters an invalid input
        while True:
            try:
                name = input("Please enter a name: ")
                #checks if the name is valid (only contains alphabets and nonspecial charcters)
                if not name.isalpha():
                    print("Names can only contain valid characters (alphabet only). Please try again.")
                    continue

                age = int(input("Please enter an age: "))
                #checks if the age is valid (from 1 to 120)
                if age < 1 or age > 120: 
                    print("Ages can only range from 1 to 120 (integers only). Please try again. ")
                    continue
                
                #asks the user if they want to input more names and ages
                retry = input("Would you want to try again? (Yes/No) ")
                #possible answers for a retry
                retry_array = ["YES", "Yes", "yes", "y", "Y", "NO", "No", "no", "n", "N"]
                #checks if the retry answer is valid, if in valid it prompts the user again
                while not retry in retry_array: 
                    retry = input("Invalid input \nWould you want to try again? (Yes/No) ")

                break

            except: 
                print("Invalid input, please try again")
                    
    #if you answer no on the retry question, it will stop the loop altogether   
        if retry in retry_array[5::]:
            break
        

    