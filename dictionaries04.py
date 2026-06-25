def getData():
    flag = True
    while flag:
        try:
            student = input("Enter the student's name or leave blank to terminate entry: ")
            if student == '':
                return '', -999  
            
            attendance = int(input('Enter the student attendance: '))
            if 0 <= attendance <= 100:
                return student, attendance  
            else:
                print('Error: Attendance must be between 0 and 100.')
                
        except ValueError:
            print("I'm sorry but this number creates an error, please aim to only have integers inputted!")

def processing():
    all_students = {}
    flag2 = True
    while flag2:
        my_student, the_attendance = getData()
        if my_student == '': 
            flag2 = False
        else:
           all_students[my_student] = the_attendance
    return all_students

# Main routine
output = processing()
for key, value in output.items():
    print(key, 'attendance is', value)