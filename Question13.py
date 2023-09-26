# Input the number of classes held and attended from the user
classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

# Calculate the attendance percentage
attendance_percentage = (classes_attended / classes_held) * 100

# Check if the student is allowed to sit in the exam
if attendance_percentage >= 75:
    print(f"Attendance Percentage: {attendance_percentage:.2f}%")
    print("The student is allowed to sit in the exam.")
else:
    print(f"Attendance Percentage: {attendance_percentage:.2f}%")
    print("The student is not allowed to sit in the exam.")
