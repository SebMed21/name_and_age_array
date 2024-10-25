#initialize the dictionary
bio_id = {}

#loop that prompts the user for input
while True:
    #Loop that retries when a user enters an invalid input
        while True:
            try:
                name = input("Please enter a name: ")
                age = int(input("Please enter an age: "))
                
                retry = input("Would you want to try again? (Yes/No) ")
                if retry != "Yes" or retry != "yes" or retry != "y":
                    raise

                break

            except: 
                print("Invalid input, please try again")

        if retry == "No" or retry == "no" or retry == "n":
            break
        

        #if you answer no on the retry question, it will stop the loop altogether   
        