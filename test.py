import time
import datetime

d = datetime.datetime.now()
d = d.replace(minute=00, hour=00, second=00)
d = (int(time.mktime(d.timetuple())))
posix = "&sday="+str(d)
print(posix)