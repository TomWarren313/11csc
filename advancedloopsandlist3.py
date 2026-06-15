def get_data():
    flag = True
    while flag:
        try:
            reps = int(input('Please enter the amount of reps you have done? '))
            if 0 < reps and reps <= 20:
                flag = False
                return reps
            
            else:
                print('Your number must be between 0 and 20!')

        except ValueError:
            print("Im sorry but this number will not work!")


def processing():
    valid_sets = []
    count = 0
    best_set = 0
    total_reps = 0
    flag2 = True
    while flag2:
        my_reps = get_data()
        valid_sets.append(my_reps)
        total_reps = total_reps + my_reps
        count = count + 1
        if my_reps > best_set:
            best_set = my_reps
            print(f'New record achieved! {best_set} is the most reps you have done, good job!')
        if total_reps >= 100:
            flag2 = False
processing()