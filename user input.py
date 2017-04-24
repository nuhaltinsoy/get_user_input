def usr_input():
    while True:
        try:
            return  str(input("Input some fantastic Craic Right Here:"))
        except ValueError:
            print("Invalid input. Come on. Try Again!")

n = usr_input()
print("*****Hooray!!!*****")
print("Here Are Your")
print("Words of Wisdom")
print("To Yourself")
print((n))
print((n))
print((n))
print("Try Again if the")
print("Craic Is Shite:")
print("********")

yes = input("Press y to try again:\n\n")

def tryagain():
    for y in yes:
            if y == "y":
                y = usr_input()
                print("*****Hooray!!!*****")
                print("Here Are Your")
                print("Here Are Your")
                print("Words of Wisdom")
                print("To Yourself")
                print((y))
                print((y))
                print((y))
                print("Try Again if the")
                print("Craic Is Shite:")
                print("********")
            else:
                print("Guess you think you have AMAZING CRAIC!! Nice one")

tryagain()

#how do we let the user try again???
