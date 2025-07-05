# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.
snum = int(input("Enter number of students: "))
total_percentage = 0  # To store sum of all student percentages

for i in range(1, snum + 1):
    print(f"\nEnter marks for Student {i} (5 subjects):")
    stu_tot_marks = 0  # Reset total marks for each student
    for j in range(1, 6):
        marks = int(input(f"  Enter marks for subject {j}: "))
        stu_tot_marks += marks  # Add marks of each subject
    
    percentage = stu_tot_marks / 5  # Calculate percentage for this student
    print(f"  Percentage of Student {i} = {percentage:.2f}%")  # Showing upto 2 decimal points
    total_percentage += percentage  # Add this student's percentage to total

# Calculate average percentage of all students
avg_percentage = total_percentage / snum
print("\nAverage Percentage of all students =", round(avg_percentage, 2), "%")
