import os
from time import time, strftime, localtime


def clear():
    os.system('clear')


def tts(t):
    return strftime('%H:%M', localtime(t))


starting_time = time()
activities = []  # activity is (name, starting time, ending time)

if __name__ == '__main__':
    print('Welcome to organizer, master')
    while True:
        print(*(f' {i + 1}\t{tts(a[1])}\t{tts(a[2])}\t{a[0]}' for i, a in enumerate(activities)), sep='\n')
        action = input(':')
        if action in ('q', 'quit'):
            quit()
        elif action in ('e', 'end'):
            activities[-1][2] = time()
        elif action.startswith('d') or action.startswith('delete'):
            try:
                index = int(action.split(' ')[1]) - 1
            except:
                index = len(activities) - 1
            try:
                activities = activities[:index] + activities[index + 1:]
            except:
                print('Wrong input')
        else:
            activities.append([action, time(), time()])
        clear()
