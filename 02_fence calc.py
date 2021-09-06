def num_check(question):


    valid = False
    while not valid:

        error1 = "please enter a number that is more than zero"
        error2 = "please enter a number"
        try:

            response = float(input(question))

            if response > 0:
                return response 

            else:
                print(error1)
                print()

        except ValueError:
            print(error2)
            print()

print()
print("***** Fence Calculator *****")
print()

looping = ""
while looping == "":

    width = num_check("width: ")
    length = num_check("length: ")
    cost_per_meter = num_check("cost/m: ")

    perimeter = 2*(width + length)
    cost = perimeter*cost_per_meter

    print("the perimeter = {:.2f} m".format(perimeter))
    print("the cost of fencing = ${:.2f}".format(cost))
    print()


    looping = input("press <enter> to continue or any key to quit")
    print()
    print("-" * 30)
    print()

print("thank you for using the Fence Calculator")
print()