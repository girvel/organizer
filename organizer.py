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
        print(*(f'{tts(a[2])}\t{tts(a[1])}\t{a[0]}' for a in activities))
        action = input(':')
        if action in ('q', 'quit'):
            quit()
        else:
            activities.append((action, time(), time()))
