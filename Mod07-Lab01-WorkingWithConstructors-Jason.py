# ------------------------------------------------- #
# Title: Lab01 - Working with Data classes
# # Description: Demonstrates how to use data classes
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# <YourNameHere>,<TheDate>,Converted dictionary rows to student class objects.
# ------------------------------------------------- #
import json

# Data -------------------------------------------- #
FILE_NAME: str = 'MyLabData.json'
MENU: str = '''
---- Student GPAs ------------------------------
  Select from the following menu:
    1. Show current student data.
    2. Enter new student data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''
students: list = []  # a table of student data
menu_choice = ''

class Student:
    """
    This class holds student data.

    Properties of class:
    - first_name (str): First name of student.
    - last_name (str): Last name of student.
    - gpa (float): Student's GPA.

    Change Log:
    Jason Coult, 12/20/2024, Created class
    """
    def __init__(self, first_name: str = '', last_name: str = '', gpa: float = 0.0):
        self.first_name = first_name  # Default first name assignment
        self.last_name = last_name  # Default last name assignment
        self.gpa = gpa  # Default last name assignment


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "r")
            #student_data = json.load(file)  # the load function returns a list of dictionary rows.
            list_of_dictionary_data = json.load(file)  # Load list of dictionary rows from the json file

            for student in list_of_dictionary_data:  # Loops through dictionary list and convert to student objects
                student_object: Student = Student(first_name = student["FirstName"],  # Grab student object properties
                                                  last_name = student["LastName"],
                                                  gpa = student["GPA"])
                student_data.append(student_object)  # Assign the new student object to student data list
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return  student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        RRoot,1.2.2030,Converted code to use student objects instead of dictionaries

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            list_of_dictionary_data = []  # Empty list to hold data for version to json-compatible format
            for student in student_data:
                #  Here, assign to dictionary entries
                student_json: dict \
                    = {"Firstname": student.first_name, "LastName": student.last_name, "GPA": student.gpa}
                list_of_dictionary_data.append(student_json)  # Convert student object back into dictionary for json

            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file)  # Write the dictionary to json file
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    """
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the a menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :return: None
        """
        print()
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def output_letter_by_gpa(student_data: list):
        """ This function displays the letter grades base on their GPA to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        RRoot,1.4.2030,Added code to toggle technical message off if no exception object is passed

        :return: None
        """
        # Process the data to create and display a custom message
        print()
        print("-" * 50)
        for student in student_data:

            if student.gpa >= 4.0:
                message = " {} {} earned an A with a {:.2f} GPA"
            elif student.gpa >= 3.0:
                message = " {} {} earned a B with a {:.2f} GPA"
            elif student.gpa >= 2.0:
                message = " {} {} earned a C with a {:.2f} GPA"
            elif student.gpa >= 1.0:
                message = " {} {} earned a D with a {:.2f} GPA"
            else:
                message = " {} {}'s {:.2f} GPA was not a passing grade"

            print(message.format(student.first_name, student.last_name, student.gpa))


            # if student["GPA"] >= 4.0:
            #     message = " {} {} earned an A with a {:.2f} GPA"
            # elif student["GPA"] >= 3.0:
            #     message = " {} {} earned a B with a {:.2f} GPA"
            # elif student["GPA"] >= 2.0:
            #     message = " {} {} earned a C with a {:.2f} GPA"
            # elif student["GPA"] >= 1.0:
            #     message = " {} {} earned a D with a {:.2f} GPA"
            # else:
            #     message = " {} {}'s {:.2f} GPA was not a passing grade"
            #
            # print(message.format(student["FirstName"], student["LastName"], student["GPA"]))

        print("-" * 50)
        print()

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the first name, last name, and GPA from the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :return: None
        """

        try:
            # Input the data
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            try:  # using a nested try block to capture when an input cannot be changed to a float
                student_gpa = float(input("What is the student's GPA? "))
            except ValueError:
                raise ValueError("GPA must be a numeric value.")

            #student = {"FirstName": student_first_name,
            #           "LastName": student_last_name,
            #           "GPA": float(student_gpa)}
            student = Student(first_name=student_first_name, last_name=student_last_name, gpa=student_gpa)
            student_data.append(student)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

#  End of function definitions


# Beginning of the main body of this script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the follow tasks
while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        IO.output_letter_by_gpa(student_data=students)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        students = IO.input_student_data(student_data=students)
        IO.output_letter_by_gpa(student_data=students)
        continue

    elif menu_choice == "3":  # Save data in a file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
