flag = True
def get_data():
    while flag:
        try:
            time_input = input('How long did you run for? ')
            run_time = int(time_input)
            if run_time > 0:
                return run_time
            else:
                print('Please enter a number greater than 0.')
        except ValueError:
            print('I am sorry, but what you entered is invalid! Try Again. ')

def process():
    held_times = []
    best_time = 0
    goal_time = 60
    flag2 = True
    while flag2:
        new_time = get_data()
        held_times.append(new_time)
        if new_time > best_time:
            best_time = new_time
            print(f'A personal best! {best_time} seconds is your best time.')
        if new_time >= goal_time:
            print('You reached your goal!')
            flag2 = False

process()