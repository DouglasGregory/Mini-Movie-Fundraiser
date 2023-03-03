# functions go here
def cash_credit(question):

    while True:
        response = input(question).lower()

        if response == "Cash" or response == "ca":
            return "Cash"
        elif response == "Credit" or response == "cr":
            return "Credit"
        else:
            print("Please enter a valid payment method")


# main routine goes here
while True:
    payment_method = cash_credit("Choose a payment method (cash"
                                 "or credit): ")

    print("You chose, Payment_method")

    print()
