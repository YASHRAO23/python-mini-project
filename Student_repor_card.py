# student report card 

student_name = str(input("Enter your name : "))
Roll_No = int(input("Enter your roll no : "))

subject = []
marks = []
num_subject = int(input("How many subjects you have? : "))

for i in range(num_subject):
    sub_name = input(f"Enter the name of subject {i+1} :")
    sub_marks = int(input(f"Enter the marks of {sub_name}: "))
    
    
    subject.append(sub_name)
    marks.append(sub_marks)
    
Total_marks = sum(marks)

max_marks = num_subject * 100

percentage = (Total_marks / max_marks)* 100

if percentage >= 90:
    grade = 'A'
elif percentage >= 75:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 45:
    grade ='D'
else:
    grade ='F (fail)'
    
print("\n" + "-"*40)
print("          STUDENT REPORT CARD         ")
print("-"*40)

print(f"Name       : {student_name}")
print(f"Roll No    : {Roll_No}\n")

print("Subjects & Marks:")
for i in range(num_subject):
    print(f"{subject[i]:<15}:{marks[i]}/100")

print("\n" + "-"*40)
print(f"Total Marks: {Total_marks} / {max_marks}")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade      : {grade}")
print("-"*40)

    