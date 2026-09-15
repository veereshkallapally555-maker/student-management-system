import json

class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["student_id"],data["name"],data["age"],data["grade"])

class StudentManager:
    def __init__(self, filename = "students.json"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Student.from_dict(student) for student in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_students(self):
        with open(self.filename, 'w') as file:
            json.dump([student.to_dict() for student in self.students], file, indent=4)

    def add_student(self, student_id, name, age, grade):
        """Adds a new student and saves to JSON."""
        # Check if ID already exists
        for student in self.students:
            if student.student_id == student_id:
                print("\n❌ Error: A student with this ID already exists!")
                return
        
        new_student = Student(student_id, name, age, grade)
        self.students.append(new_student)
        self.save_students()
        print(f"\n✅ Student '{name}' added successfully!")

    def view_students(self):
        """Displays all saved students."""
        if not self.students:
            print("\n⚠️ No student records found.")
            return

        print("\n====== Student Records ======")
        for index, student in enumerate(self.students, start=1):
            print(f"{index}. ID: {student.student_id} | Name: {student.name} | Age: {student.age} | Grade: {student.grade}")

    def search_student(self, search_query):
        """Searches for a student by ID or Name."""
        found = False
        print(f"\n====== Search Results for '{search_query}' ======")
        for student in self.students:
            if search_query.lower() in student.student_id.lower() or search_query.lower() in student.name.lower():
                print(f"🆔 ID: {student.student_id} | 👤 Name: {student.name} | 🎂 Age: {student.age} | 🎓 Grade: {student.grade}")
                found = True
        
        if not found:
            print("❌ No matching student found.")

    def delete_student(self, student_id):
        """Deletes a student by ID."""
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.save_students()
                print(f"\n🗑️ Student ID '{student_id}' deleted successfully!")
                return
        
        print("\n❌ Error: Student ID not found.")

def main():
    manager = StudentManager()

    while True:
        print("\n====== Student Management System (OOP) ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter Choice (1-5): ").strip()

        if choice == "1":
            try:
                student_id = input("Enter Student ID: ").strip()
            except ValueError:
                print("❌ Invalid input! Student ID must be a number.")
                continue
            name = input("Enter Name: ").strip()

            if not name:
                print("❌ Name cannot be empty.")
                continue
           try:
                age = int(input("Enter Age: ").strip())

                if age <= 0 or age > 100:
                    print("❌ Invalid age! Please enter an age between 1 and 100.")
                    continue

            except ValueError:
                print("❌ Invalid input! Age must be a number.")
                continue
            try:
                grade = input("Enter Grade (e.g., A, B, C): ").strip().upper()
            except ValueError:
                print("❌ Invalid input! Grade must be a string.")
                continue

            manager.add_student(student_id, name, age, grade)

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            query = input("Enter Student ID or Name to search: ").strip()
            manager.search_student(query)

        elif choice == "4":
            try:
                student_id = input("Enter Student ID to delete: ").strip()
                manager.delete_student(student_id)
            except ValueError:
                print("❌ Invalid input! Student ID must be a number.")

        elif choice == "5":
            print("\n👋 Exiting Student Management System. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
