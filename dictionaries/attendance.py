student_attendance = {"Rolf": 96, "Aian": 80, "Anne": 100}

# For loop
# for student in student_attendance:
#     print(f"{student}: {student_attendance[student]}")

# Better way
# for student, attendance in student_attendance.items():
#     print(f"{student}: {attendance}")


# if "Bob" in student_attendance:
#     print(f"Bob: {student_attendance['Bob']}")
# else:
#     print("Bob is not a student in this class.")

# Getting the values without the keys
attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))