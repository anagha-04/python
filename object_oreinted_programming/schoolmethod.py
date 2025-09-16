

class Student:
    school_name ="ABCD"
    def __init__(self,roll,name,total):

        self.roll = roll

        self.name = name

        self. total = total

    @classmethod   
    def update_school_name(cls,new_class_name):

        cls.school_name= new_class_name

        print(cls.school_name)

    @staticmethod
    def is_pass(total):

        return True if total>140 else False
    
student_instance1 = Student(12,"hari",145)

student_instance2 =Student(32,"gopika",130)

Student.update_school_name("CMS")

print(Student.is_pass(student_instance1.total))

print(Student.is_pass(student_instance2.total))
        
    