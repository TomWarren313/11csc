'''
This program uses a dictionary to sort out student averages. It will then print them all out
'''

def getData():
    flag = True
    while flag:
        try:
            student = input("Enter the student's name or leave blank to terminate entry: ").title()
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
    total = 0
    all_students = {}
    flag2 = True
    while flag2:
        my_student, the_attendance = getData()
        if my_student == '': 
            average = total / len(all_students)
            flag2 = False
        else:
           total = total + the_attendance
           all_students[my_student] = the_attendance
    return all_students, average

def output():
  print()
  print('Results entered. Now printing attendance and overall average')
  output, my_average = processing()
  for key, value in output.items():
      print(f"{key}'s", 'attendance is', f"{value}%")
  print(f'Average attendance throughout all students: {my_average}%')

#main routine
output()