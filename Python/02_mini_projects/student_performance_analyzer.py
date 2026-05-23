def calculate_average(marks):
    average = sum(marks) / len(marks)
    return average

def assign_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 75:
        return "B"
    elif average >=60:
        return "C"
    else:
        return "Need Improvement"
    

def generate_report(student):
    name = student["name"]
    marks = student["marks"]

    average = calculate_average(marks)
    grade = assign_grade(average)

    print("Student Performance Report")
    print("--------------------------")
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Average: {average}")
    print(f"Grade: {grade}")


student_data = {
    "name": "Neelam",
    "marks": [85, 90, 78, 92, 88]
}

generate_report(student_data)