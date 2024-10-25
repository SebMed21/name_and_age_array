#initialize the dictionary
bio_id = {}

#loop that prompts the user for input
while True:
    #Loop that retries when a user enters an invalid input
        while True:
            try:
                name = input("Please enter a name: ")
                age = int(input("Please enter an age: "))
                
                #asks the user if they want to input more names and ages
                retry = input("Would you want to try again? (Yes/No) ")
                #possible answers for a retry
                retry_array = ["YES", "Yes", "yes", "y", "Y", "NO", "No", "no", "n", "N"]
                while not retry in retry_array: 
                    retry = input("Invalid input \nWould you want to try again? (Yes/No) ")

                break

            except: 
                print("Invalid input, please try again")
                    
    #if you answer no on the retry question, it will stop the loop altogether   
        if retry in retry_array[5::]:
            break
        

    