from datetime import datetime

class Student:
    def __init__(self, StudentID, Name, DOB, classification):
        self.__ID = StudentID
        self.__Name = Name
        self.__DOB = datetime.strptime(DOB, "%m/%d/%Y")
        self.__class = classification

    def set_ID(self, StudentID):
        self.__ID = StudentID

    def set_Name(self, Name):
        self.__Name = Name

    def set_DOB(self, DOB):
        self.__DOB = datetime.strptime(DOB, "%m/%d/%Y")

    def set_Class(self, classification):
        self.__class = classification

    def get_ID(self):
        return self.__ID

    def get_Name(self):
        return self.__Name

    def get_DOB(self):
        return self.__DOB

    def get_class(self):
        return self.__class

    def calculate_age(self):
        today = datetime.today()
        dob_date = self.__DOB
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        return age

    def get_registration_dates(self):
        registration_dates = {
            "Senior": "4/1 thru 4/3",
            "Junior": "4/4 thru 4/6",
            "Sophomore": "4/7 thru 4/9",
            "Freshman": "4/10 thru 4/12"
        }
        return registration_dates.get(self.__class, "Unknown")

    def get_age(self):
        return self.calculate_age()

    def get_registration_period(self):
        return self.get_registration_dates()
