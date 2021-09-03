"""
class - student
"""
class Student():
    '''
    attributes
    '''
    name=''
    course=''
    sem=0
    rollno=0
    address=''
    '''
    functionality
    '''
    def enrollStudent(self,name,course,sem,rollno,address):
        self.name = name
        self.course = course
        self.sem = sem
        self.address= address        
    def showStudent(self):
        student = ' Name : ',self.name,' Course : ',self.course
        return student
'''
student1 is an object
'''
student1 = Student()
student1.enrollStudent('Ravi','BCA',4,100,'55,Hebbal,Bengaluru')
info= student1.showStudent()
print('information about student 1 ',info)
'''
student2 is an object
'''
student2 = Student()
student2.enrollStudent('Rohit','BCA',4,101,'56,Yelahanka,Bengaluru')
info= student2.showStudent()
print('information about student 2 ',info)






