def check_access (registered, lab_open, computer_available):
    if registered == "Y" and lab_open == "Y" and computer_available == "Y":
        return "Acces Granted"
    else:
        return "Acces Denied"
    
def get_reason (registered, lab_open, computer_available):
    if registered != "Y":
        return "Student is not registered"
    elif lab_open != "Y":
        return "The Lab is not open"
    elif computer_available != "Y":
        return "There are no available Computers in the Lab"
    else:
        return "Welcome to the Lab!"
