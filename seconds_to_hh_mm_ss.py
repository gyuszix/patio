#convert seconds to hours minutes and seconds
def make_readable(seconds):

    hours = seconds // 3600
    right_hours = str(hours)
    if len(right_hours) == 1:
        right_hours = '0' + right_hours

    minutes = seconds % 3600 // 60
    right_minutes = str(minutes)
    if len(right_minutes) == 1:
        right_minutes = '0' + right_minutes

    seconds = seconds % 3600 % 60
    right_seconds = str(seconds)
    if len(right_seconds) == 1:
        right_seconds = '0' + right_seconds

    answer = f'hh:mm:ss \n{right_hours}:{right_minutes}:{right_seconds}'

    return answer



