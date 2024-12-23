# ------------------------------------------------- #
# Title: Lab01 - Working with Constructors
# # Description: Demonstrates how to use class constructors
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# RRoot,1.2.2030,Converted dictionary rows to student class objects.
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


# TODO 1. add student class
class Student:
    """
    A class representing student data.

    Properties:
    - first_name (str): The student's first name.
    - last_name (str): The student's last name.
    - gpa (float): The gpa of the student.

    ChangeLog:
    - RRoot, 1.1.2030: Created the class.
    """

    def __init__(self, first_name: str = '', last_name: str = '', gpa: float = 0.00):
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Converted code to use student objects instead of dictionaries
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        RRoot,1.5.2030,Converted list of dictionaries to list of student objects

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows to be filled with file data

        :return: list
        """
        try:
            file = open(file_name, "r")

            # TODO 2. Change variable name to represent that this is a list of Json dictionary objects
            # student_data = json.load(file)
            list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.

            # TODO 3. Add code to convert the Json dictionary objects to student objects
            for student in list_of_dictionary_data:
                student_object: Student = Student(first_name=student["FirstName"],
                                                  last_name= student["LastName"],
                                                  gpa=student["GPA"])
                student_data.append(student_object)

            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

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
            # TODO 4. Create a new list to hold Json data to use with the json.dump() function.
            list_of_dictionary_data: list = []

            # TODO 5. Add code to convert the list of Student objects to Json compatible list of dictionaries.
            for student in student_data:
                student_json: dict \
                    = {"FirstName": student.first_name, "LastName": student.last_name, "GPA": student.gpa}
                list_of_dictionary_data.append(student_json)

            file = open(file_name, "w")

            # TODO 6. Change the first argument to be the list of dictionary data
            json.dump(list_of_dictionary_data, file)
            # json.dump(student_data, file)
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
    RRoot,1.5.2030,Converted methods to use student objects instead of dictionaries
    """
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

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

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: None
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def output_letter_by_gpa(student_data: list):
        """ This function displays the letter grades base on their GPA to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        RRoot,1.2.2030,Converted code to use student objects instead of dictionaries

        :param student_data: list of student object data to be displayed

        :return: None
        """
        print()
        print("-" * 50)
        for student in student_data:

            # TODO 7. Replace using dictionary keys with using object attributes

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

            # print(message.format(student["FirstName"], student["LastName"], student["GPA"]))

        print("-" * 50)
        print()

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the first name, last name, and GPA from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        RRoot,1.2.2030,Converted code to use student objects instead of dictionaries

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
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

            # TODO 8. Replace using a dictionary with using a student object
            student = Student(first_name=student_first_name, last_name=student_last_name, gpa=student_gpa)
            student_data.append(student)

            # student = {"FirstName": student_first_name,
            #            "LastName": student_last_name,
            #            "GPA": float(student_gpa)}

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
