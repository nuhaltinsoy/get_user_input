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
