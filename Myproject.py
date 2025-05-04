# Converted Python Code from C++ version
import os
import time
import pickle

class Science:
    def __init__(self):
        self.id = 0
        self.table = 0
        self.name = ""
        self.gender = ""
        self.dob = ""
        self.center = ""
        self.room = ""
        self.math = 0.0
        self.biology = 0.0
        self.khmer = 0.0
        self.history = 0.0
        self.physics = 0.0
        self.chemistry = 0.0
        self.english = 0.0

    def input_data(self):
        self.id = int(input("Input Student ID          : "))
        self.name = input("Input Student Name         : ")
        self.gender = input("Input Student Gender       : ")
        self.dob = input("Input Student D_O_B        : ")
        self.table = int(input("Input Student Table        : "))
        self.room = input("Input Student Room         : ")
        self.center = input("Input Student Center       : ")
        while True:
            self.math = float(input("Input Score Math       [125] : "))
            self.biology = float(input("Input Score Biology    [75]  : "))
            self.physics = float(input("Input Score Physics    [75]  : "))
            self.chemistry = float(input("Input Score Chemistry  [75]  : "))
            self.khmer = float(input("Input Score Khmer      [75]  : "))
            self.history = float(input("Input Score History    [50]  : ")) - 25
            self.english = float(input("Input Score English    [50]  : ")) - 25

            if (0 < self.math <= 125 and
                0 < self.biology <= 75 and
                0 < self.physics <= 75 and
                0 < self.chemistry <= 75 and
                0 < self.khmer <= 75 and
                -25 < self.history <= 25 and
                -25 < self.english <= 25):
                break
            else:
                print("Invalid scores entered. Please try again.")

    def total(self):
        return self.math + self.biology + self.physics + self.chemistry + self.khmer + self.history + self.english

    def total_rank(self):
        return self.total() / 4.75

    def grade(self):
        total = self.total()
        if 427 <= total <= 475:
            return 'A'
        elif 380 <= total < 427:
            return 'B'
        elif 332 <= total < 380:
            return 'C'
        elif 285 <= total < 332:
            return 'D'
        elif 237 <= total < 285:
            return 'E'
        else:
            return 'F'

    def display(self):
        print(f"{self.id:07d} {self.name:21} {self.gender:9} {self.dob:15} {self.table:7} {self.room:7} {self.center:13} {self.total():13.2f} {self.total_rank():15.2f} {self.grade()}")

class User:
    def __init__(self):
        self.username = ""
        self.password = ""

    def register(self):
        self.username = input("Enter email      : ")
        self.password = input("Enter password   : ")
        confirm = input("Confirm password : ")
        while self.password != confirm:
            print("Password does not match!")
            self.password = input("Enter password   : ")
            confirm = input("Confirm password : ")
        print("Register Successful!")

    def login(self):
        email = input("Enter email      : ")
        password = input("Enter password   : ")
        return self.username == email and self.password == password

def loading_animation():
    print("\n\t\t\tLOADING", end="")
    for _ in range(20):
        print(".", end="", flush=True)
        time.sleep(0.1)
    print("\nLoading Complete!\n")
    time.sleep(0.5)
    os.system('clear' if os.name == 'posix' else 'cls')

def save_students(students, filename='Science.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(students, file)

def load_students(filename='Science.pkl'):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

# Main menu logic here (use input to handle cases similar to the C++ switch statement)
# Additional features (search, update, delete, insert, sort, etc.) can be implemented similarly.
