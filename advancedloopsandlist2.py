best_time = 0
goal_time = 50
flag = True
held_times = []
def get_data():
    while flag:
        try:
            time_input = input('How long did you run for? ')
            run_time = int(time_input)
            if run_time > 0:
                held_times.append(run_time)
                return run_time
            else:
                print('Please enter a number greater than 0.')
        except ValueError:
            print('I am sorry, but what you entered is invalid! Try Again. ')

flag2 = True
while flag2:
    run_time = get_data()

    if run_time > best_time:
      best_time = run_time
      print(f'A personal best! {best_time} seconds is your best time.')

    if run_time >= goal_time:
      print('You reached your goal!!!')
      flag2 = False

print('Recording ended.')

if len(held_times) == 0:
  print('Sorry, you have not entered any valid times.')
else:
  print('Your results are:')

held_times.sort(reverse= True)
for num in held_times:
  print(num, 'seconds')