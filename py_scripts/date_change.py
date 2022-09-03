import os
import time
import datetime
from pathlib import Path

def setTime(year,month,day,hour,minute,second):
    date = datetime.datetime(year=int(year),month=int(month),day=int(day),hour=int(hour),minute=int(minute),second=int(second))
    modTime = time.mktime(date.timetuple())
    os.utime(directory, (modTime,modTime))


directory_name = 'C:\\Users\\ziolk\\Desktop\\Pictures'

for filename in os.listdir(directory_name):
    directory = os.path.join(directory_name, filename)

    if filename[0:3] == 'IMG' or filename[0:3] == 'VID':
        year = filename[4:8]
        month = filename[8:10]
        day = filename[10:12]
        hour = filename[13:15]
        minute = filename[15:17]
        second = filename[17:19]
        setTime(year, month, day, hour, minute, second)
        Path(directory).rename(directory_name+'2\\'+filename)

    elif filename[0:3] == 'Scr':
        year = filename[11:15]
        month = filename[16:18]
        day = filename[19:21]
        hour = filename[22:24]
        minute = filename[25:27]
        second = filename[28:30]
        # print(' '.join([year,month,day,hour,minute,second]))
        setTime(year,month,day,hour,minute,second)
        Path(directory).rename(directory_name+'2\\'+filename)







