

class Student:

    id: int

    name: str

    course: str

    address: str

    def set_student(self,id,name,course,address):

        self.id = id

        self.name = name

        self.course = course

        self.address = address

    def display_student(self):

        print(self.id,self.name,self.course,self.address)

student_instance1 = Student()

student_instance2 = Student ()       

student_instance1.set_student(100,"anoka","bsc cs","abcd street")

student_instance1.display_student()