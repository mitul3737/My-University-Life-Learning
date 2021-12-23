class Exam:
    def __init__(self, marks):
        self.marks = marks
        self.time = 60

    def examSyllabus(self):
        return "Maths , English"

    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"


class ScienceExam(Exam):
    part_1 = []
    part_2 = ""
    part_3 = ""

    def __init__(self, marks, time, *args):
        self.part = 2
        super().__init__(marks)
        self.time = time
        self.part_0 = [] #important one
        for i in args:
            self.part_0.append(i)
            self.part += 1

    def examSyllabus(self):
        self.part_1 = super().examSyllabus().split(" , ")
        for j in self.part_0:
            self.part_1.append(j)
        for k in self.part_1:
            self.part_2 += k + " , "

        return self.part_2[:-3]

    def examParts(self):
        for x in range(1, len(self.part_1) + 1):
            self.part_3 += f"Part {x} - {self.part_1[x - 1]}\n"
        return self.part_3[:-1]

    def __str__(self):
        return f"Marks: {self.marks} Time: {self.time} minutes Number of\nParts: {self.part}"


engineering = ScienceExam(100, 90, "Physics", "HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================')
architecture = ScienceExam(100, 120, "Physics", "HigherMaths", "Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())

"""Marks: 100 Time: 90 minutes Number of
Parts: 4
----------------------------------
Maths , English , Physics , HigherMaths
Part 1 - Maths
Part 2 - English
Part 3 - Physics
Part 4 - HigherMaths
==================================
Marks: 100 Time: 120 minutes Number of
Parts: 5
----------------------------------
Maths , English , Physics , HigherMaths
, Drawing
Part 1 - Maths
Part 2 - English
Part 3 - Physics
Part 4 - HigherMaths
Part 5 - Drawing"""