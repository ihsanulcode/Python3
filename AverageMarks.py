#1.
#There are five students and take input of their math, English, physics, and chemistry course marks.
# Find the average of each course marks.

math = []
english = []
physics = []
chemistry = []


print("Enter Math course marks for 5 students:")
for i in range(1,6):
    marks = float(input())
    math.append(marks)

print("Enter English course marks for 5 students:")
for i in range(1,6):
    marks = float(input())
    english.append(marks)

print("Enter physics course marks for 5 students:")
for i in range(1,6):
    marks = float(input())
    physics.append(marks)

print("Enter chemistry course marks for 5 students:")
for i in range(1,6):
    marks = float(input())
    chemistry.append(marks)

print("\nAverage of Math course marks:", sum(math) / len(math))
print("Average of English course marks:", sum(english) / len(english))
print("Average of Physics course marks:", sum(physics) / len(physics))
print("Average of chemistry course marks:", sum(chemistry) / len(chemistry))
