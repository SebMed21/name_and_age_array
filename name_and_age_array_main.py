#initialize the dictionary
bio_id = {}

#loop that prompts the user for input
while True:
    #Loop that retries when a user enters an invalid input
        while True:
            try:
                name = input("Please enter a name: ")
                age = int(input("Please enter an age"))

                retry = input("Would you want to try again? ")

                #Stops the nested loop
                break
            
            except: 
                print("Invalid input")
