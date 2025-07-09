class Student:
    def __init__(self):
        self.name = ""
        self.group = ""
        self.spanish_score = 0.0
        self.english_score = 0.0
        self.socials_score = 0.0
        self.science_score = 0.0

    def student_entry(self):
        self.name = input("Enter student's name: ")
        self.group = input("Enter student's group: ")

        def get_score(subject):
            while True:
                try:
                    score = float(input(f"Enter {subject} score (0-100): "))
                    if 0 <= score <= 100:
                        return score
                    else:
                        print("Invalid score! Must be between 0 and 100.")
                except ValueError:
                    print("Oops! That was not a valid number. Try again.")

        self.spanish_score = get_score("Spanish")
        self.english_score = get_score("English")
        self.socials_score = get_score("Socials")
        self.science_score = get_score("Science")

    def display_student(self):
        return {
            "Name": self.name,
            "Group": self.group,
            "Spanish Score": self.spanish_score,
            "English Score": self.english_score,
            "Socials Score": self.socials_score,
            "Science Score": self.science_score
        }

# Example usage:
student1 = Student()  # ✅ Creates an empty student object
student1.student_entry()  # ✅ Asks user for input
print(student1.display_student())  # ✅ Shows stored student data
