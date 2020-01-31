# from time import localtime,strftime, time
# #use this for calculating the time between clock in and out
# #store this variable in a json file that can be drawn upon later
#     #five days {"in":start_time, "hours_worked_today": hours_worked}
#         #no need to keep the "done" or "out" variable because the localtime will be recorded in a second file.
#     #new json object for each day? then you can grab the hours_worked for each day and add them up easily
# start = time()
#
# done = time()
# elapsed = done - start
# print(elapsed)
#
#
# #write this to a json file or csv to record start and end time for record keeping
#
# current_time = strftime("%H:%M", localtime())
#
# print(current_time)
#
#
# #how do i use this method if i need to clock in or out for a different time other than current time.
#
from datetime import datetime, timedelta
import os
import json
import time

def total_hours(timecard):
    #dont call before clock out!
    total = timedelta()
    for i in range(0, len(timecard), 2):
        _in = datetime.fromisoformat(timecard[i]["time"])
        _out = datetime.fromisoformat(timecard[i+1]["time"])
        total+= _out - _in
    print(total)


def clock_in():
    current_time = datetime.now()
    day_of_week = current_time.weekday()
    monday = current_time - timedelta(days=day_of_week)
    file_name = f"{monday.strftime('%y_%m_%d')}.json"
    if not os.path.exists(file_name):
        with open(file_name, "w+") as f:
            json.dump([],f)
    with open(file_name, "r") as f:
        timecard = json.load(f)
    timecard.append({
        "time":current_time.isoformat(),
        "type":"In",
    })
    with open(file_name, "w") as f:
        json.dump(timecard, f)

    #confimation, hours left in work week 40-hours worked

def clock_out():
    current_time = datetime.now()
    day_of_week = current_time.weekday()
    monday = current_time - timedelta(days=day_of_week)
    file_name = f"{monday.strftime('%y_%m_%d')}.json"
    with open(file_name, "r") as f:
        timecard = json.load(f)
    timecard.append({
        "time":current_time.isoformat(),
        "type":"out",
    })
    total_hours(timecard)
    with open(file_name, "w") as f:
        json.dump(timecard, f)




def todays_hours(timecard):
    filter(lambda x:x, timecard)
    pass

def hours_remain():
    pass

clock_in()
time.sleep(2)
clock_out()
