from datetime import timedelta,datetime

# tt = input("Enter total time (HH.MM):").split('.')
# tt = timedelta(hours=int(tt[0]),minutes=int(tt[1]))

def conv_time(function):
    def inner(time):
        func,flag = function(time)
        if flag==1:
            func = str(func)+" "+str('PM')
        elif flag==0:
            func = str(func)+" "+str('AM')
        return func
    return inner


@conv_time
def format_time(time):
    days,seconds = time.days,time.seconds
    hrs = days * 24 + seconds // 3600
    mins = (seconds % 3600) // 60
    if hrs%13>=0:
        return timedelta(hours=hrs%13+1,minutes=mins),1
    else:
        return timedelta(hours=hrs%13,minutes=mins),0



tt = timedelta(hours=7,minutes=30)


flag = 0
c = 0
timeseries = []
timelist = []
while True:
    if flag==0:
        intime = input("In time (HH.MM):").split('.')
        intime = timedelta(hours=int(intime[0]),minutes=int(intime[1]))
        timeseries.append(intime)
        flag = 1
    elif flag==1:
        outtime = input("Out time (HH.MM):").split('.')
        outtime = timedelta(hours=int(outtime[0]),minutes=int(outtime[1]))
        timeseries.append(outtime)
        flag = 0
    c += 1
    if c%2==0:
        timelist.append(outtime-intime)
    ch = input("Enter more?(y=1/n=0): ")
    if int(ch)==0:
        break

entrytime = timeseries[0]
sumtime = timedelta(hours=0,minutes=0)
for i in timelist:
    sumtime += i
    
now = datetime.now().strftime('%H:%M').split(':')
now = timedelta(hours=int(now[0]),minutes=int(now[1]))


if c==1:
    averagebreak = timedelta(minutes=25)
    print('\nExit time: ',format_time(entrytime + averagebreak + tt))
    print('Exit time (24HR format): ',entrytime + averagebreak + tt)
elif c%2==1:
    print("\nRemaining Hours: ",tt-sumtime)
    print("Remaining from",format_time(now),":", ((timeseries[-1]+(tt-sumtime))-(now)))
    print("Exit time: ",format_time(timeseries[-1]+(tt-sumtime)))
    print("Exit time (24HR format): ",timeseries[-1]+(tt-sumtime))
else:
    print("\nExit time without breaks(expected): ",format_time(entrytime+tt))
    print("Exit time without breaks(expected) 24HR format: ",entrytime+tt)
    print("Break taken: ",(timeseries[-1]-entrytime)-sumtime)
    print("Total hours spent: ",sumtime)