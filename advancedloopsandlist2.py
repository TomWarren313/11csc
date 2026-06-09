held_times = []
def get_data():
    try:
        time = input('Please enter a time: ')
        time = int(time)
        if time > 0:
            held_times.append(time)
    except ValueError:
        print('Im sorry but what you entered is invalid! Try Again.')
    return time