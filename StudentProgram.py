import StudentClass as s

def main():
    # Creating an instance of the Student class
    student = s.Student("8915555", "John Smith", "02/29/2000", "Junior")

    # Displaying the age of the student
    print("Age of the student:", student.get_age())

    # Displaying when the student can register
    print("Registration period:", student.get_registration_period())


main()
