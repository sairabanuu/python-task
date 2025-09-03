class Student:
    class_name='10thclass'
    def stu1(self,roll_no,subject,marks):
        print(roll_no,subject,marks)
    
    def stu2(self,roll_no,subject,marks):
        print(roll_no,subject,marks)
    
    def stu3(self,roll_no,subject,marks):
      print(roll_no,subject,marks)
    
    def stu4(self,roll_no,subject,marks):
        print(roll_no,subject,marks)
        
    def avg(self):
        print(self.stu_name,self.id,self.total,self.per)
    
    @classmethod
    def change_class(cls,new_class_name):
        cls.class_name=new_class_name
        
    @staticmethod
    def programs():
        print("programs: anualday")
s1=Student()
s2=Student()
s1.stu1(101,'hindi',50)
s1.stu1(102,'telugu',80)
s1.stu1(103,'english',70)
s1.stu1(104,'science',65)

s1.stu_name='saira'
s1.id=1
s1.total=470
s1.per=70

s2.stu_name='banu'
s2.id=2
s2.total=430
s2.per=65

s1.avg()
s2.avg()

Student.change_class("9thclass")
print("class_name:",Student.class_name)

Student.programs()