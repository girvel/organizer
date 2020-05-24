import os
import platform
from time import time, strftime, localtime, gmtime
import termcolor


def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')


def tts(t, relative=False):
    return strftime('%H:%M', (gmtime if relative else localtime)(t))


starting_time = time()
activities = []  # activity is (name, starting time, ending time)

if __name__ == '__main__':
    clear()
    print('Welcome to organizer, master')
    input()
    while True:
        clear()
        total_time = (activities[-1][2] - starting_time) if activities else 0
        print(
            termcolor.colored(
                'Started at {started}{tab1}Now is {current}{tab2}Spent {spent}\n'.format(
                    started=tts(starting_time),
                    current=tts(time()),
                    spent=tts(total_time, True),
                    tab1=' ' * 14,
                    tab2=' ' * 18,
                ),
                "grey",
                "on_white"
            )
        )
        print(*(f' {i + 1}\t{tts(a[1])}\t{tts(a[2])}\t{a[0]}' for i, a in enumerate(activities)), sep='\n')
        print()
        if activities:
            parts = dict()
            for a in activities:
                if a[0] not in parts:
                    parts[a[0]] = 0
                parts[a[0]] += a[2] - a[1]
            print(
                *(
                    '{percentage}%\t{time}\t{activity}'.format(
                        percentage=round(v / total_time * 100),
                        time=tts(v, True),
                        activity=k) for k, v in {**parts, "doing nothing": total_time - sum(parts.values())}.items()
                ),
                sep='\n',
                end='\n\n'
            )
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
