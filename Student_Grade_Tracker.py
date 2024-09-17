def display_menu():
    print("\n--- Student Grade Tracker Menu ---")
    print("1. Add Student Grades")
    print("2. Calculate Average Grade")
    print("3. Determine Letter Grade")
    print("4. View All Grades")
    print("5. Exit")
    print("-----------------------------------")

def add_student_grades(grades):
    student_name = input("Enter the student's name: ")
    grade = float(input(f"Enter the grade for {student_name}: "))
    
    if student_name in grades:
        grades[student_name].append(grade)
    else:
        grades[student_name] = [grade]
    
    print(f"Grade {grade} added for {student_name}.")

def calculate_average(grades):
    student_name = input("Enter the student's name to calculate average: ")
    
    if student_name in grades:
        average = sum(grades[student_name]) / len(grades[student_name])
        print(f"The average grade for {student_name} is: {average:.2f}")
    else:
        print(f"No grades found for {student_name}.")

def determine_letter_grade(grades):
    student_name = input("Enter the student's name to determine letter grade: ")
    
    if student_name in grades:
        average = sum(grades[student_name]) / len(grades[student_name])
        letter_grade = ''
        
        if average >= 90:
            letter_grade = 'A'
        elif average >= 80:
            letter_grade = 'B'
        elif average >= 70:
            letter_grade = 'C'
        elif average >= 60:
            letter_grade = 'D'
        else:
            letter_grade = 'F'
        
        print(f"The letter grade for {student_name} is: {letter_grade}")
    else:
        print(f"No grades found for {student_name}.")

def view_all_grades(grades):
    if not grades:
        print("No students and grades available.")
        return
    
    print("\n--- All Student Grades ---")
    for student, grade_list in grades.items():
        print(f"{student}: {grade_list}")
    print("--------------------------")

def main():
    grades = {}
    
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_student_grades(grades)
        elif choice == '2':
            calculate_average(grades)
        elif choice == '3':
            determine_letter_grade(grades)
        elif choice == '4':
            view_all_grades(grades)
        elif choice == '5':
            print("Exiting the grade tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()