import os
from time import time, strftime, localtime


def clear():
    os.system('clear')


def tts(t):
    return strftime('%H:%M', localtime(t))


starting_time = time()
activities = []  # activity is (name, starting time, ending time)

if __name__ == '__main__':
    clear()
    print('Welcome to organizer, master')
    input()
    while True:
        clear()
        total_time = (activities[-1][2] - starting_time) if activities else 0
        print(f'Started at {tts(starting_time)}\t\tNow is {tts(time())}\t\tSpent {tts(total_time - 18000)}\n')
        print(*(f' {i + 1}\t{tts(a[1])}\t{tts(a[2])}\t{a[0]}' for i, a in enumerate(activities)), sep='\n')
        print()
        if activities:
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
            print()
        action = input(':')
        if not action:
            continue
        elif action in ('exit', 'quit'):
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
        elif action.startswith('s') or action.startswith('save'):
            try:
                name = action.split(' ')[1]
            except:
                print('Name is required')
                continue
            with open(name, 'w') as f:
                f.write(str(starting_time))
                f.write('\n')
                f.write('\n'.join('\t'.join(str(e) for e in a) for a in activities))
        elif action.startswith('open'):
            try:
                name = action.split(' ')[1]
            except:
                print('Name is required')
                continue
            with open(name, 'r') as f:
                content = f.read().split('\n')
            starting_time = float(content[0])
            content = content[1:]
            if not content[-1]:
                content = content[:-1]
            content = [e.split('\t') for e in content]
            print(content)
            activities = [[e[0], float(e[1]), float(e[2])] for e in content]
        else:
            activities.append([action, time(), time()])
