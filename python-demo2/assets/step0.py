import datetime

def t1():
    #исправьте строчку ниже
    day  = 'Day of week: ' + str(datetime.datetime.today().weekday())
    return day

print(t1())