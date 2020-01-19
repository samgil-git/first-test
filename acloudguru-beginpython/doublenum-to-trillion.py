# GOAL
# starting with a number, double it until at least 1 trillion

# make sure the user enters a valid number
def inputNumber(message):
    while True:
        try:
            userInput = float(input(message))
        except ValueError:
            print("Not a number, try again.")
            continue
        else:
            return userInput
            break


# put user input to a variable
start_num = inputNumber("Choose a number: ")

# loop to keep doubling the variable until it will exceed 1 trillion
while start_num <= 1000000000000:
    print(str(start_num))
    start_num *= 2
