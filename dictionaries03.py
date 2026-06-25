'''
This program aims to get students names and attedance average and then prints out them all in a neat list
'''

def getData():
    student =''
    attendance = -999  
    flag = True
    while flag:
        try:
          student = input('Enter the students name or leave blank to terminate entry : ')
          if student == '':
             flag = False
          else:
            attendance = int(input('Enter the student attendance: '))
            if attendance >= 0 and attendance <= 100:
               student = input('Enter the students name or leave blank to terminate entry : ')
            else:
               print('Error boundary message')
            return student,attendance
          
        except ValueError:
           print('Im sorry but this number creates an error, please aim to only have integers inputted!')

def processing():
   total = 0
   all_students = {}
   flag2 = True
   while flag2:
      my_student,the_attendance = getData()
      while my_student != '':
         total = total + the_attendance
         all_students[my_student] = the_attendance
         my_student,the_attendance = getData()
      flag = False


#main routine
output = processing()
for key, value in output.items():
  print(key, 'average is', value)
