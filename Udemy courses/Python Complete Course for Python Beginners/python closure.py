def print_message(message):#a closure function
    def print_message_inner():
        print(message) # print_message_inner can access this message variable
    return print_message_inner
val=print_message("Assalamualaikum!") # print_message has been passed with a value "Assalamualaikum"
#and val has the reference then of print_message_inner . so it can be said as the print_message_inner
val() #calling print_message_inner