class Student:
    def __init__(self, name, age, grade, id):
        self.name = name
        self.age = age
        self.grade = grade
        self.id = id
    
class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} has been enrolled in the school.")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"{student.name} has been removed from the school.")
        else:
            print(f"{student.name} is not enrolled in the school.")

    def list_students(self):
        print("List of Students:")
        for student in self.students:
            print(f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}, ID: {student.id}")

def main():
    school = School()
    while True:
        print("\nOptions:")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. List Students")
        print("4. Quit")
        choice = input("Enter choice (1-4): ")

        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = int(input("Enter student grade: "))
            id = input("Enter student ID: ")
            student = Student(name, age, grade, id)
            school.add_student(student)

        elif choice == "2":
            id = input("Enter student ID: ")
            student = next((s for s in school.students if s.id == id), None)
            if student:
                school.remove_student(student)
            else:
                print(f"Student with ID {id} not found.")

        elif choice == "3":
            school.list_students()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
