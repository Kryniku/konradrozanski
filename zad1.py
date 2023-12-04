class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50

student1 = student("Maciuś",[40,60,70,80,20])
student2 = student("Natalia",[10,20,30,20,20])

print(f"{student1.name} zaliczył: {student1.is_passed()}")
print(f"{student2.name} zaliczył: {student2.is_passed()}")