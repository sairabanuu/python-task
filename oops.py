class Calculator:
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def mul(self,a,b):
        print(a*b)
    def div(self,a,b):
        print(a/b)
    def describe(self):
        print(self.model_num,self.made_in,self.color,self.discount)
        
c1=Calculator()
c2=Calculator()

c1.add(2,3)
c1.sub(40,20)
c1.mul(3,4)
c1.div(2,4)

c1.model_num=432
c1.made_in='India'
c1.color='blue'
c1.discount=300

c2.model_num=4323
c2.made_in='china'
c2.color='red'
c2.discount=200
c1.describe()
c2.describe()


# define self
# it is a refernce to the current object of the class
# whenever you create an object,self allows the attributes and methods of that object
# it is a passed automatically as the first parameter in all instance methods of a class
# by convention we use the name self,but u can use any name