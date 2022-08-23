import requests

###users ='pepito'
###cpuinf ='54545' 

monitoring_report = {'users': 'Carlos', 'cpuinfo': '12345'}
resp = requests.post('192.168.1.11:8080/servers/monitoring', data=monitoring_report)