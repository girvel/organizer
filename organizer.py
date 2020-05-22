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
        elif action in ('s', 'stats', 'statistics'):
            print()
            total_time = time() - starting_time
            parts = dict()
            for a in activities:
                if a[0] not in parts:
                    parts[a[0]] = 0
                parts[a[0]] += a[2] - a[1]
            sum = 0
            for k, v in parts.items():
                sum += v
                v = round(v / total_time * 100)
                print(f'{v}%\t{k}')
            print(f'{round((1 - sum / total_time) * 100)}%\tDoing nothing')
            input()
        else:
            activities.append([action, time(), time()])
        clear()
