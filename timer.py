import time

def countdown(user_time):
    while user_time:
        mins, secs = divmod(user_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        user_time -= 1
        print(user_time)

user_time=input("Podaj czas: ")
countdown(int(user_time))
