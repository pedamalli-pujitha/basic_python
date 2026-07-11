# student attendance checker:

Total=int(input("Enter total classes:"))
attended=int(input("Enter attended classes:"))
percentage=(attended/Total)*100
print("Attendance percentage:",percentage)
if percentage>=75:
  print("Eligible for Exam")
else:
  print("Not Eligible for Exam")