def get_student():
    print("===== Computer Lab Access =====" )

    name = input("Enter your name: ")
    student_id = input("Enter your student id: ")

    registered = input("Are you registered for today's Lab? (Y/N): ").upper()
    lab_open = input("Is the Lab open Today (Y?N): ").upper()
    computer_available = input("Is there available Computer's in the Lab? (Y/N): ").upper()

    return name, student_id, registered, lab_open, computer_available