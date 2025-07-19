# variables are called = attributes = att
# functions are called = methods
# classes can't be empty - use pass if need to
# method def arg = self
# self represents the object calling it (e.g. student1) 


# Created a class with 2 methods
'''
class student:
    def check_pass_fail(self): # method
        if self.marks >= 50:
            return True
        else:
            return False
        
    def __init__(self, name, marks): # first patrameter self rep the object calling it i.e. student1
        self.name = name
        self.marks = marks
        

student1 = student("Harry", 85) # object 1
# create an object, init method is called automatically with the values Harry and 85

student2 = student("Janet", 45) # object 2


print(student1.name)
print(student1.marks)
did_pass = student1.check_pass_fail()
print(did_pass)

print(student2.name)
print(student2.marks)
did_pass = student2.check_pass_fail()
print(did_pass)




#2

class complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image
    
    def add(self, number): # self = n1 number = n2
        real = self.real + number.real # n1 5 + n2 -4
        image = self.image +number.image # n1 6 + n2 2
        result = complex(real, image)  
        return result
        
n1 = complex(5, 6)
n2 = complex(-4,2)
result = n1.add(n2) # call add method on n1 object and passed n2 object to it

print("real =", result.real)
print("image =", result.image)

'''


# 3

class triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def get_perimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter
    
t1 = triangle(3, 4, 5)
perimeter = t1.get_perimeter()
print("The perimeter of the triangel is", perimeter)