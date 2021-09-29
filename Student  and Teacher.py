import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS teeacherss  ( 
    id INTEGER PRIMARY KEY, 
    name TEXT,
    surname TEXT
    date_birthday TEXT
)""")
db.commit()

sql.execute("""CREATE TABLE IF NOT EXISTS student  ( 
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT
)""")
db.commit()

sql.execute("""CREATE TABLE IF NOT EXISTS subject  (
    id INTEGER PRIMARY KEY, 
    subject TEXT
)""")
db.commit()

sql.execute("""CREATE TABLE IF NOT EXISTS gruppa  ( 
    id INTEGER PRIMARY KEY,
    number_group TEXT
)""")
db.commit()


class Teacher:

    def delete_data_teachers(self):
        del_name = input('Input the first name you want to delete: ')
        del_surname = input('Input the last name you want to delete: ')

        sql.execute(f"SELECT name, surname FROM teeacherss WHERE name = '{del_name}' AND surname = '{del_surname}'")
        if sql.fetchone():
            sql.execute(f"DELETE FROM teeacherss WHERE name = '{del_name}' AND surname = '{del_surname}'")
            db.commit()

            print('The entry was deleted')

        else:
            print('There is no such record')

            for value in sql.execute("SELECT * FROM teeacherss"):
                print(value)

    def adding_data_teachers(self):
        teacher_name = input('Input name: ')
        teacher_surname = input('Input surname: ')
        sql.execute(
            f"SELECT name, surname FROM teeacherss WHERE name = '{teacher_name}' AND surname = '{teacher_surname}' ")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO teeacherss VALUES (?,?)", (teacher_name, teacher_surname))
            db.commit()

            print('Entry added')

        else:
            print('Such an entry is already available')

            for value in sql.execute("SELECT * FROM teeacherss"):
                print(value)

    def view_data_teachers(self):
        for value in sql.execute("SELECT * FROM teeacherss"):
            print(value)

    def points_teacher(self):
        while True:
            print("******************************")
            print("  Options of db Teachers")
            print("******************************")
            print("1. View data")
            print("2. Add data")
            print("3. Delete data")
            print("4. Return to main page")
            print("5. Exit")

            n = int(input("\nSelect your choice : "))

            if n == 1:
                self.view_data_teachers()
            elif n == 2:
                self.adding_data_teachers()
            elif n == 3:
                self.delete_data_teachers()
            elif n == 4:
                self.home()
            elif n == 5:
                print("Thank you!!")
                exit()
            else:
                print("Invalid option!\n try again\n")
                self.points_teacher()


class Student:

    def delete_data_student(self):

        del_name = input('Input the first name u want to delete: ')

        del_surname = input('Input the last name u want to delete: ')

        sql.execute(f"SELECT name, surname FROM student WHERE name = '{del_name}' AND surname = '{del_surname}'")
        if sql.fetchone():
            sql.execute(f"DELETE FROM student WHERE name = '{del_name}' AND surname = '{del_surname}'")
            db.commit()

            print('The entry was deleted')

        else:
            print('There is no such record')

            for value in sql.execute("SELECT * FROM student"):
                print(value)

    def adding_data_student(self):

        student_name = input('Input name: ')
        student_surname = input('Input surname: ')

        sql.execute(f"SELECT name, surname FROM student WHERE name = '{student_name}' AND surname = '{student_surname}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO student VALUES (?,?)", (student_name, student_surname))
            db.commit()

            print('Entry added')

        else:
            print('Such an entry is already available')

            for value in sql.execute("SELECT * FROM student"):
                print(value)

    def view_data_student(self):
        for value in sql.execute("SELECT * FROM student"):
            print(value)

    def points_student(self):
        while True:
            print("******************************")
            print("  Options of db Student ")
            print("******************************")
            print("1. View data")
            print("2. Add data")
            print("3. Delete data")
            print("4. Return to main page")
            print("4. Exit")

            n = int(input("\nSelect your choice : "))
            if n == 1:
                self.view_data_student()
            elif n == 2:
                self.adding_data_student()
            elif n == 3:
                self.delete_data_student()
            elif n == 4:
                self.home()
            elif n == 5:
                print("Thank You!)")
                exit()
            else:
                print("Invalid option!\n try again\n")
                self.points_student()


class Subject:
    def delete_data_subject(self):
        del_subject = input('Input the first name u want to delete: ')

        sql.execute(f"SELECT subject FROM subject WHERE subject = '{del_subject}'")
        if sql.fetchone():
            sql.execute(f"DELETE FROM subject WHERE subject = '{del_subject}'")
            db.commit()

            print('The entry was deleted')

        else:
            print('There is no such record')

            for value in sql.execute("SELECT * FROM subject"):
                print(value)

    def adding_data_subject(self):
        subject_data = input('Input subject that u want to add: ')

        sql.execute(f"SELECT name, surname FROM student WHERE name = '{subject_data}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO student VALUES (?)", (subject_data,))
            db.commit()

            print('Entry added')

        else:
            print('Such an entry is already available')

            for value in sql.execute("SELECT * FROM student"):
                print(value)

    def view_data_subject(self):
        for value in sql.execute("SELECT * FROM subject"):
            print(value)

    def points_subject(self):
        while True:
            print("******************************")
            print("  Options of db Subject")
            print("******************************")
            print("1. View data")
            print("2. Add data")
            print("3. Delete data")
            print("4. Return to main page")
            print("5. Exit")

            n = int(input("\nSelect your choice : "))
            if n == 1:
                self.view_data_subject()
            elif n == 2:
                self.adding_data_subject()
            elif n == 3:
                self.delete_data_subject()
            elif n == 4:
                self.home()
            elif n == 5:
                print("Thank You!)")
                exit()
            else:
                print("Invalid option!\n try again\n")
                self.points_subject()


class Group:

    def delete_data_group(self):
        del_number_group = input('Input the first name u want to delete: ')

        sql.execute(f"SELECT number_group FROM gruppa WHERE number_group = '{del_number_group}'")
        if sql.fetchone():
            sql.execute(f"DELETE FROM gruppa WHERE number_group = '{del_number_group}'")
            db.commit()

            print('The entry was deleted')

        else:
            print('There is no such record')

            for value in sql.execute("SELECT * FROM gruppa"):
                print(value)

    def adding_data_group(self):
        num_group = input('Input subject that u want to add: ')

        sql.execute(f"SELECT number_group FROM gruppa WHERE number_group = '{num_group}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO gruppa VALUES (?)", (num_group,))
            db.commit()

            print('Entry added')

        else:
            print('Such an entry is already available')

            for value in sql.execute("SELECT * FROM gruppa"):
                print(value)

    def view_data_group(self):
        for value in sql.execute("SELECT * FROM gruppa"):
            print(value)

    def points_group(self):
        while True:
            print("******************************")
            print("  Options of db Group")
            print("******************************")
            print("1. View data")
            print("2. Add data")
            print("3. Delete data")
            print("4. Return to main page")
            print("5. Exit")

            n = int(input("\nSelect your choice : "))
            if n == 1:
                self.view_data_group()
            elif n == 2:
                self.adding_data_group()
            elif n == 3:
                self.delete_data_group()
            elif n == 4:
                self.home()
            elif n == 5:
                print("Thank You!)")
                exit()
            else:
                print("Invalid option!\n try again\n")
                self.points_group()


class Main:

    def home(self):
        while True:
            print("******************************")
            print("  Main page ")
            print("******************************")
            print("1. Teacher")
            print("2. Student")
            print("3. Subject")
            print("4. Group")
            print("5. Exit")

            n = int(input("\nSelect your choice : "))
            if n == 1:
                teacher = Teacher()
                teacher.points_teacher()
            elif n == 2:
                student = Student()
                student.points_student()
            elif n == 3:
                subject = Subject()
                subject.points_subject()
            elif n == 4:
                group = Group()
                group.points_group()
            elif n == 5:
                print("Thank You!)")
                exit()
            else:
                print("Invalid option!\n try again\n")
                self.home()


main_page = Main()
main_page.home()