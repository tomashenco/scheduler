import sys
from datetime import datetime, timedelta


def give_next():
    fields = raw_input('Type command (type "end" to finish): ').split()

    if 'end' in fields:
        print 'Closing tool'
        return 0

    try:
        minute, hour, command = fields
    except ValueError:
        print 'Need to specify 3 fields'
        return 1

    minute_list = [str(x).zfill(2) for x in range(60)] if minute == '*' else [minute.zfill(2)]
    hour_list = [str(x) for x in range(24)] if hour == '*' else [hour, ]
    target = [h+':'+m for h in hour_list for m in minute_list]

    time = min(target, key=delta)
    h, m = time.split(':')
    day = 'today' if datetime(1, 1, 1, int(h), int(m)) >= now else 'tomorrow'
    print time, day, command

    return 1


if __name__ == '__main__':
    current_hour, current_minute = sys.argv[1].split(':')
    now = datetime(1, 1, 1, hour=int(current_hour), minute=int(current_minute))

    def delta(x):
        h, m = x.split(':')
        t = datetime(1, 1, 1, hour=int(h), minute=int(m))
        return t - now if t >= now else timedelta.max

    while True:
        result = give_next()
        if not result:
            break
