# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes with structured error handling.
# The assignment is built upon a starter script provided by RRoot.
#
# Change Log: (Who, When, What)
#   Jason Coult, 12/22/2024, Created script based on RRoot starter code
#   Jason Coult, 12/23/2024, Modified script to meet requirements of assignment
# ------------------------------------------------------------------------------------------ #
import json  # For working with json files

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # List of student objects
menu_choice: str  # Menu input choice from user

class Person:
    """
    Class defining a person.

    Properties:
        - first_name (str): The person's first name.
        - last_name (str): The person's last name.

    Changelog:
        Jason Coult, 12/22/2024, Created class
        Jason Coult, 12/23/2024, Modified properties
    """

    # Person constructor
    def __init__(self, first_name: str = '', last_name: str = ''):
        self.first_name = first_name  # First name
        self.last_name = last_name  # Last name

    # Person first name getter and setter
    @property  # Getter
    def first_name(self):
        return self.__first_name.title()  # Format first name to title case

    @first_name.setter  # Setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":  # Allow only letters in text
            self.__first_name = value
        else:  # Other error
            raise ValueError("The first name should only use letters!")

    # Person last name getter and setter
    @property  # Getter
    def last_name(self):
        return self.__last_name.title()  # Format in title case

    @last_name.setter  # Setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":  # Allow only letters in text
            self.__last_name = value
        else:  # Other error
            raise ValueError("The last name should only use letters!")

    # Person string function
    def __str__(self):  # Override default str method to show info about person
        return f'{self.first_name} {self.last_name}'  # Fstring for output

class Student(Person):
    """
    Class defining a student, inherited from Person.

    Properties:
        - first_name (str): Inherits person's first name.
        - last_name (str): Inherits person's last name.
        - course_name (str): Student's course name. 

    Changelog:
        Jason Coult, 12/23/2024, Created class
    """

    # Student constructor
    def __init__(self, first_name: str = '', last_name: str = '', course_name: str = ''):
        super().__init__(first_name = first_name, last_name = last_name)  # Parent class (person) constructor
        self.course_name = course_name  # Course name

    # Course name getter and setter
    @property  # Getter
    def course_name(self):
        return self.__course_name.title()  # Format course name title case too

    @course_name.setter  # Setter
    def course_name(self, value: str):
        self.__course_name = value  # No error check b/c course name can be alphanumeric

    # Student string function
    def __str__(self):  # Override with custom string function
        return f'{self.first_name} {self.last_name}, {self.course_name}'


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    Jason Coult, 12/23/2024, Created class based on RRoot's starter code
    Jason Coult, 12/23/2024, Modified class to be compatible with objects
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and loads it into a list of student objects

        ChangeLog: (Who, When, What)
        Jason Coult, 12/23/2024, Created function based on RRoot's starter code
        Jason Coult, 12/23/2024, Modified function to work with objects

        :param file_name: String data with name of file to read from
        :param student_data: List of objects, created from file rows, to be filled with file data

        :return: list
        """

        try:
            file = open(file_name, "r")  # Open file in read mode
            list_of_dictionary_data = json.load(file)  # Assign to list of dictionaries
            for individual_student in list_of_dictionary_data:  # Loop through the rows in dictionary list
                individual_student_object: Student = Student(  # Pull out using keys and assign to object properties
                    first_name = individual_student["FirstName"],
                    last_name = individual_student["LastName"],
                    course_name = individual_student["CourseName"]
                )
                student_data.append(individual_student_object)  # Add on to list of student objects

            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file.closed == False:
                file.close()  # Close just in case try block failed and file remains open
        return student_data  # Return the list of student objects

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file

        ChangeLog: (Who, When, What)
        Jason Coult, 12/23/2024, Created based on RRoot's starter code
        Jason Coult, 12/23/2024, Modified to work with student objects

        :param file_name: string data with name of file to write to
        :param student_data: list of student objects to be writen to the file

        :return: None
        """

        try:
            file = open(file_name, "w")  # Open file in write mode
            list_of_dictionary_data: list = []  # Empty list to hold student rows converted from student objects
            for individual_student in student_data:  # Loop through each student object
                student_row: dict = {  # Create dictionary entry with object property values as key-value pairs
                    "FirstName": individual_student.first_name,
                    "LastName": individual_student.last_name,
                    "CourseName": individual_student.course_name}
                list_of_dictionary_data.append(student_row)  # Append the dictionary row to the list
            json.dump(list_of_dictionary_data, file, indent=4)  # Save data & format it nicely within the file
            file.close()
            IO.output_student_and_course_names(student_data=student_data)  # Display the list for reference
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog:
    Jason Coult, 12/23/2024, Created based on RRoot's starter code
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays custom error messages to the user

        ChangeLog:
        Jason Coult, 12/23/2024, Created based on RRoot's starter code

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog:
        Jason Coult, 12/23/2024, Created function based on RRoot's starter code

        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog:
        Jason Coult, 12/23/2024, Created function based on RRoot's starter code
        Jason Coult, 12/23/2024, Update with more detailed input error
        :return: string with the users choice
        """
        choice = ""  # To check if nothing has been entered
        try:
            choice = input("Enter your menu choice number: ")  # User input prompt
            if len(choice) == 0:  # Error case for no input
                raise Exception("No choice made. Please enter a choice!")
            elif choice not in ("1", "2", "3", "4"):  # Error case for invalid selection
                raise Exception("Please only chose 1,2,3,4")
        except Exception as e:
            IO.output_error_messages(e.__str__(), e)  # Display the particular error message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog:
        Jason Coult, 12/23/2024, Created function based on RRoot's starter code
        Jason Coult, 12/23/2024, Modified function to use student objects

        :param student_data: list of student objects to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:  # Loop through each object in list and print property values
            print(f'Student {student.first_name} {student.last_name} is enrolled in {student.course_name}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog:
        Jason Coult, 12/23/2024, Created function based on RRoot's starter code
        Jason Coult, 12/23/2024, Modified for use with student objects

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            # Create student object one property at a time using sequential user prompts. Each property is assigned with
            # each prompt in order to trigger an immediate error to user if a bad value is entered.
            student_object = Student(first_name = input("Enter the student's first name: "))  # Student + first name
            student_object.last_name = input("Enter the student's last name: ")  # Add last name is first name valid
            student_object.course_name = input("Please enter the name of the course: ")  # Add course if last name valid
            student_data.append(student_object)  # Append student object
            print()
            print(f'You have registered '
                  f'{student_object.first_name} {student_object.last_name} for {student_object.course_name}.')
        except ValueError as e:
            IO.output_error_messages(message="One of the values was not the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of student objects
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    # Get the user's input
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
