#Declare control variables
total = 0
entries = 0

#Continually asks the user to enter a number
while True:
    number = int(input("Enter a number or -1 to stop: "))

    #Specify a condition when the loop ends
    if number == -1:
        break
    #Increase control variables in the loop
    total += number
    entries += 1

    #Average of the numbers entered, excluding the -1
    average = total / entries

#Blank line to help readibility
print("")

#Output
if entries > 0:
    print(f"The average of the entered numbers is: {average}")
else:
    print("No numbers were entered.")

# End-of-file (EOF)
