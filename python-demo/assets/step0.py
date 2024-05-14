import datetime

def t1():
    return 'Day of week: ' + str(datetime.datetime.today().weekday())

print(t1())