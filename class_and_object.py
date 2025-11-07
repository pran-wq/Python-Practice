class Student:
    # Constructor - initializes object attributes
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks  # Dictionary of subject:marks

    # Method to display student details
    def display_info(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")

    # Method to calculate average marks
    def average_marks(self):
        avg = sum(self.marks.values()) / len(self.marks)
        return avg

    # Method to check grade
    def grade(self):
        avg = self.average_marks()
        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "Fail"


# --- Creating Objects ---
student1 = Student("Pranav", 101, {"Math": 95, "Science": 88, "English": 92})
student2 = Student("Rashmi", 102, {"Math": 72, "Science": 65, "English": 70})

# --- Displaying Info ---
student1.display_info()
print("Average Marks:", student1.average_marks())
print("Grade:", student1.grade())

student2.display_info()
print("Average Marks:", student2.average_marks())
print("Grade:", student2.grade())
