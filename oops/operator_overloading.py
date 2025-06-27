class two_student_marks:
    def __init__(self,first,second):
        self.first = first
        self.second = second

    def __add__(self, other):
        m1 = self.first + other.first
        m2 = self.second + other.second
        return m1+m2

s1 = two_student_marks(10,20)
s2 = two_student_marks(10,20)
print(s1+s2)