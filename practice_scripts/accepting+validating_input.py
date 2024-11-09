#Testing converting inputs and ensuring a correct input

def user_input():
    # DEFINE INITIAL VARIABLES
    choice ='No'
    acceptable_input = range(0,11)
    within_range = False

    # GET USER INPUT WITH CONDITTIONS
    # ALWAYS CHECK IF USER INPUT IS A NUMBER AND IN RANGE
    while choice.isdigit() == False or within_range == False:

        choice = input("Please enter a number (0-10): ")

        if choice.isdigit() == False: # IF USER INPUT IS NOT A NUMBER
            print ("That's not a number!") # PRINT ERROR MESSAGE AND TRY AGAIN

        if choice.isdigit(): # IF USER INPUT IS A NUMBER
            if int(choice) in acceptable_input: # CHECK IF USER INPUT IS IN RANGE
                within_range = True # SET within_range TO TRUE IF USER INPUT IS IN RANGE
                break # BREAK OUT OF LOOP IF USER INPUT IS IN RANGE
            else:
                print ("Your choice is not in range") # PRINT ERROR MESSAGE IF USER INPUT IS NOT IN RANGE AND TRY AGAIN
                pass # SAME AS LEAVING withing_range = False
    return int(choice)
                

user_input()
# TRY RUNNING THE FUNCTION A FEW TIMES TO CHECK FOR INPUT VALIDITY