import os
import pickle
import time
# hellloooo fdsafadsfjdsalfj 
# --- Color Functions ---
def reset():
    print("\033[0m", end='')

def red():
    print("\033[1;31m", end='')

def green():
    print("\033[0;32m", end='')

def yellow():
    print("\033[0;33m", end='')

def blue():
    print("\033[0;34m", end='')

def purple():
    print("\033[0;35m", end='')

def cyan():
    print("\033[0;36m", end='')

def false_grade_color():
    print("\033[0;101m", end='')

# --- Grade Color ---
def color_grade(grade):
    if grade == 'A' or grade == 'B':
        red()
    elif grade == 'C':
        yellow()
    elif grade == 'D':
        green()
    elif grade == 'E':
        blue()
    else:
        reset()

# --- Header Display ---
def header():
    cyan()
    print(f"\n{'ID':<7}{'Name':<22}{'Gender':<9}{'DOB':<15}{'Table':<7}{'Room':<7}{'Center':<13}"
          f"{'Total_Score':<14}{'Total_Rank':<15}"
          f"{'Math':<7}{'Biology':<10}{'Khmer':<8}{'Physics':<10}{'Chemistry':<12}{'History':<10}{'English':<10}Grade")
    reset()

# --- Science Class ---
class Science:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.gender = ""
        self.dob = ""
        self.table = 0
        self.room = ""
        self.center = ""
        self.math = 0
        self.biology = 0
        self.physics = 0
        self.chemistry = 0
        self.khmer = 0
        self.history = 0
        self.english = 0

    def input_data(self):
        green()
        self.id = int(input("\nInput Student ID: "))
        self.name = input("Input Student Name: ")
        self.gender = input("Input Student Gender: ")
        self.dob = input("Input Student D_O_B: ")
        self.table = int(input("Input Student Table: "))
        self.room = input("Input Student Room: ")
        self.center = input("Input Student Center: ")

        while True:
            try:
                self.math = float(input("Input Score Math [125]: "))
                self.biology = float(input("Input Score Biology [75]: "))
                self.physics = float(input("Input Score Physics [75]: "))
                self.chemistry = float(input("Input Score Chemistry [75]: "))
                self.khmer = float(input("Input Score Khmer [75]: "))
                self.history = float(input("Input Score History [50]: "))
                self.english = float(input("Input Score English [50]: "))

                if not (0 < self.math <= 125):
                    raise ValueError("Math invalid.")
                if not (0 < self.biology <= 75):
                    raise ValueError("Biology invalid.")
                if not (0 < self.physics <= 75):
                    raise ValueError("Physics invalid.")
                if not (0 < self.chemistry <= 75):
                    raise ValueError("Chemistry invalid.")
                if not (0 < self.khmer <= 75):
                    raise ValueError("Khmer invalid.")
                if not (0 < self.history <= 50):
                    raise ValueError("History invalid.")
                if not (0 < self.english <= 50):
                    raise ValueError("English invalid.")
                break
            except ValueError as e:
                print("\nInvalid input:", e)
        
        self.history -= 25
        self.english -= 25
        reset()

    def total(self):
        return self.math + self.biology + self.physics + self.chemistry + self.khmer + self.history + self.english

    def total_rank(self):
        return self.total() / 4.75

    def grade(self):
        t = self.total()
        if 427 <= t <= 475:
            return 'A'
        elif 380 <= t < 427:
            return 'B'
        elif 332 <= t < 380:
            return 'C'
        elif 285 <= t < 332:
            return 'D'
        elif 237 <= t < 285:
            return 'E'
        else:
            return 'F'

    def sub100(self):
        if 112 <= self.math <= 125:
            return 'A'
        elif 100 <= self.math < 112:
            return 'B'
        elif 87 <= self.math < 100:
            return 'C'
        elif 75 <= self.math < 87:
            return 'D'
        elif 67 <= self.math < 75:
            return 'E'
        else:
            return 'F'

    def sub75(self, score):
        if 67 <= score <= 75:
            return 'A'
        elif 60 <= score < 67:
            return 'B'
        elif 52 <= score < 60:
            return 'C'
        elif 45 <= score < 52:
            return 'D'
        elif 37 <= score < 45:
            return 'E'
        else:
            return 'F'

    def sub50(self, score):
        if 20 <= score <= 25:
            return 'A'
        elif 15 <= score < 20:
            return 'B'
        elif 10 <= score < 15:
            return 'C'
        elif 5 <= score < 10:
            return 'D'
        elif 0 < score < 5:
            return 'E'
        else:
            return 'F'

    def output_data(self):
        grade_result = self.grade()
        if grade_result == 'F':
            false_grade_color()
        print(f"{self.id:07d}    {self.name:<21}{self.gender:<9}{self.dob:<15}{self.table:<7}{self.room:<7}{self.center:<13}", end='')
        red()
        print(f"{self.total():<14}", end='')
        reset()
        print(f"{self.total_rank():<15}", end='')

        color_grade(self.sub100())
        print(f"{self.sub100():<7}", end='')
        reset()
        color_grade(self.sub75(self.biology))
        print(f"{self.sub75(self.biology):<10}", end='')
        reset()
        color_grade(self.sub75(self.khmer))
        print(f"{self.sub75(self.khmer):<8}", end='')
        reset()
        color_grade(self.sub75(self.physics))
        print(f"{self.sub75(self.physics):<10}", end='')
        reset()
        color_grade(self.sub75(self.chemistry))
        print(f"{self.sub75(self.chemistry):<12}", end='')
        reset()
        color_grade(self.sub50(self.history))
        print(f"{self.sub50(self.history):<10}", end='')
        reset()
        color_grade(self.sub50(self.english))
        print(f"{self.sub50(self.english):<10}", end='')
        reset()
        color_grade(grade_result)
        print(f"{grade_result}")
        reset()

# --- User Data Class ---
class UserData:
    def __init__(self):
        self.username = ""
        self.password = ""

    def register(self):
        green()
        print("\n|-----------------------------------------|")
        print("|==========++++REGISTER SYSTEM++++===========|")
        print("|-----------------------------------------|")
        self.username = input("|Enter email      : ")
        self.password = input("|Enter password   : ")
        confirm = input("|Confirm password : ")

        if self.password != confirm:
            red()
            print("Password does not match..!")
            reset()
            self.register()

    def login(self):
        green()
        print("\n|-----------------------------------------|")
        print("|==========++++LOGIN SYSTEM++++===========|")
        print("|-----------------------------------------|")
        email = input("|Enter email      : ")
        password = input("|Enter password   : ")

        if email == self.username and password == self.password:
            loading_animation()
            green()
            print("Login Successful..!")
            reset()
            return True
        else:
            red()
            loading_animation()
            print("Email or Password incorrect!")
            reset()
            return False

# --- Loading Animation ---
def loading_animation():
    purple()
    print("\n\t\t\tLOADING", end='')
    for _ in range(20):
        print(".", end='', flush=True)
        time.sleep(0.1)
    print("\nLoading Complete!\n")
    reset()

# --- File Operations ---
def save_students(students):
    with open("Science.bin", "wb") as f:
        pickle.dump(students, f)

def load_students():
    if not os.path.exists("Science.bin"):
        return []
    with open("Science.bin", "rb") as f:
        return pickle.load(f)

# --- Main ---
def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    user = UserData()
    students = load_students()

    while True:
        green()
        print("\n ===============================| MENU |================================")
        print("|                               1.Register                                 |")
        print("|                               2.Login                                    |")
        print("|                               3.Exit                                     |")
        print(" ========================================================================")
        reset()
        choice = input("Enter your option: ")

        if choice == '1':
            user.register()
            loading_animation()
            print("Register Successful..!")

        elif choice == '2':
            if user.login():
                while True:
                    cyan()
                    print("\n ===============================| MENU |================================")
                    print("|                               A.Write                                 |")
                    print("|                               B.Read                                  |")
                    print("|                               C.Search                                |")
                    print("|                               D.Update                                |")
                    print("|                               E.Delete                                |")
                    print("|                               F.Insert                                |")
                    print("|                               G.Sort                                  |")
                    print("|                               0.Exit                                  |")
                    print(" ========================================================================")
                    reset()
                    sub_choice = input("Please Select One option: ").lower()

                    if sub_choice == 'a':
                        n = int(input("Input number of students: "))
                        for _ in range(n):
                            student = Science()
                            student.input_data()
                            students.append(student)
                        save_students(students)

                    elif sub_choice == 'b':
                        header()
                        for student in students:
                            student.output_data()

                    elif sub_choice == 'c':
                        search_choice = input("Search by (1) ID or (2) Name? ")
                        if search_choice == '1':
                            sid = int(input("Enter ID: "))
                            header()
                            for s in students:
                                if s.id == sid:
                                    s.output_data()
                        elif search_choice == '2':
                            sname = input("Enter Name: ")
                            header()
                            for s in students:
                                if s.name.lower() == sname.lower():
                                    s.output_data()

                    elif sub_choice == 'd':
                        sid = int(input("Enter ID to update: "))
                        for i, s in enumerate(students):
                            if s.id == sid:
                                students[i].input_data()
                                save_students(students)
                                print("Update Successful..!")
                                break
                        else:
                            print("Student not found.")

                    elif sub_choice == 'e':
                        sid = int(input("Enter ID to delete: "))
                        students = [s for s in students if s.id != sid]
                        save_students(students)
                        print("Delete Successful..!")

                    elif sub_choice == 'f':
                        sid = int(input("Enter ID to insert before: "))
                        for i, s in enumerate(students):
                            if s.id == sid:
                                new_student = Science()
                                new_student.input_data()
                                students.insert(i, new_student)
                                save_students(students)
                                print("Insert Successful..!")
                                break
                        else:
                            print("Student not found.")

                    elif sub_choice == 'g':
                        students.sort(key=lambda x: x.total_rank(), reverse=True)
                        save_students(students)
                        print("Sort Successful..!")

                    elif sub_choice == '0':
                        break

        elif choice == '3':
            exit()

if __name__ == "__main__":
    main()
