order=input("What do you want to print SID,name or class:") 
def student_data(student_id,**data):
    if order=="sid":
            print("\nStudent ID:",student_id)
    elif order=="name" or order=="class":
            print("Student name:",{data['student_name']}, "Student class:",{data['student_class']})
            print("\n")
    



student_data(21102068, student_name="Rudransh", student_class="B.tech")
student_data(21102069, student_name="Dev Bohat",student_class="B.tech")
student_data(21102074, student_name="Lapata", student_class="B.tech")
