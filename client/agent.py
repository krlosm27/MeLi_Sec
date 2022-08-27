import subprocess
from subprocess import check_output
import json
import requests

sessions = check_output(["who"]).decode("UTF-8")
cpuinf = check_output(["lscpu"]).decode("UTF-8")
os = check_output(['cat /etc/*release* | grep -E -i PRETTY_NAME'], shell=True).decode("UTF-8")
ver_os = check_output(['cat /etc/*release* | grep -E -i ^VERSION_ID'], shell=True).decode("UTF-8")
process = check_output(["ps -ef"], shell=True).decode("UTF-8")
process = process.replace('\\', '/')
date = check_output(["date"]).decode("UTF-8")
ip_server = check_output(["ifconfig | grep 'inet ' | grep -v '127.0.0.1' | awk -F ' ' '{print $2}'"], shell=True).decode("UTF-8")

monitoring = {
    'commands': {
        'users': sessions,
        'cpu_info': cpuinf,
        'operative_system': os,
        'version_os': ver_os,
        'process': process
    }
}


def monitoring_report(serverURL, jsonString):
    headers = {'Content-type': 'application/json'}
    resp = requests.post(serverURL, data=json.dumps(jsonString), headers=headers)
    print(resp.text)


monitoring_report('http://192.168.1.11:8080/servers/monitoring', monitoring)
    