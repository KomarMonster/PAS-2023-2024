import ntplib
from time import ctime

c = ntplib.NTPClient()
response = c.request('ntp.task.gda.pl')
print(ctime(response.tx_time))