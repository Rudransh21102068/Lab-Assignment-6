class Student:
    pass

class Marks:
    pass

name1 = Student()
fail = Marks()
print(isinstance(name1, Student))
print(isinstance(fail, Student))
print(isinstance(fail, Marks)) 
print(isinstance(name1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
