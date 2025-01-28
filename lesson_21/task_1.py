import logging
from datetime import datetime, timedelta

logging.basicConfig(
    filename='hb_test.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

with open('hblog.txt', 'r') as f:
    content = f.read()
    print(type(content))

logs_list = content.split('\n')

key = 'Key TSTFEED0300|7E3E|0400'
filtered_log = [log for log in logs_list if key in log]

key_time = 'Timestamp'
time_list = [log[log.find(key_time) + len(key_time) + 1: log.find(key_time) + len(key_time) + 9] for log in filtered_log]

time_object_list = [datetime.strptime(time_str, "%H:%M:%S") for time_str in time_list]

for count in range(0, len(time_object_list) - 1, 2):
    heart_beat = time_object_list[count] - time_object_list[count + 1]
    if timedelta(seconds=33) > heart_beat > timedelta(seconds=31):
        logging.warning(f"WARNING: Heartbeat у допустимому діапазоні: {heart_beat}")
    elif heart_beat > timedelta(seconds=33):
        logging.error(f"ERROR: Heartbeat за межаим допустимого діапазону: {heart_beat}")
