# functions go here

# checks user has entered yes / no toa question
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no")


# checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("sorry this can't be blank. Please try again")
        else:
            return response

# main routine starts here

# set maximum number of tickets below


MAX_TICKETS = 3
ticket_sold = 0

# ask user if they want to see the instructions
want_instructions = yes_no("Do you want to read the instructions")

if want_instructions == "yes":
    print("instructions go here")

print()
# loop to sell tickets

while ticket_sold < MAX_TICKETS:
    name = not_blank("Enter your name (or 'xxx' to quit) ")

    if name == 'xxx':
        break

    ticket_sold += 1

# output number of tickets sold
if ticket_sold == MAX_TICKETS:
    print("congratulations you have sold all the tickets")
else:
    print("you have sold {} ticket/s.  There is {} ticket/s "
          "remaining".format(ticket_sold, MAX_TICKETS - ticket_sold))
