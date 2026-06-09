best_time = 0
goal_time = 60
held_times = []
flag = True
#Defining our def to get our required data.
def check_time():
    time = int(input('How long did you hold your breath? '))
    if time > 0:
      held_times.append(time)
    return time

while flag:
  try:
    my_time = check_time()

    if my_time > best_time:
      best_time = my_time
      print(f'A personal best! {best_time} seconds is your best time.')

    if my_time >= goal_time:
      print('You reached your goal!!!')
      flag = False

  except ValueError:
    flag = False
print('Recording ended.')

if len(held_times) == 0:
  print('Sorry, you have not entered any valid times.')
else:
  print('Your results are:')

held_times.sort(reverse= True)
for num in held_times:
  print(num, 'seconds')