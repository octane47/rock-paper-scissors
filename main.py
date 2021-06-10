# Functions go here
def choice_checker(question):

  error = "please choose from rock / paper / " \ "scissors (or xxx to quit)"
#main routine goes here

  vaild = False
  while not vaild:

    #ask user for choice and check it's vaild
    response = input(question).lower()
  
    if response == "r" or response == "rock":
      return response
    elif response == "p" or response == "paper":
      return response

# print out choice for comparison purposes
