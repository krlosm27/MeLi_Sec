import subprocess
from subprocess import check_output
import json
import requests

sessions = check_output(["who"])
cpuinf = check_output(["lscpu"])
os = check_output(['cat /etc/*release* | grep -E -i PRETTY_NAME'], shell=True)
ver_os = check_output(['cat /etc/*release* | grep -E -i ^VERSION_ID'], shell=True)
process = check_output(['ps -ef | sed "s/u/o/g" | grep -v sed'], shell=True)
process = check_output(["ps -ef | sed 's/\\/\/\//g' | grep -v sed"])
date = check_output(["date"])
ip_server = check_output(["ip addr show"])

nombreArchivo = ver_os.decode("UTF-8") + date.decode("UTF-8") + ".json" # concatenado de nombre de archivo json

monitoring = {
    'commands': {
        'users': sessions.decode("UTF-8"),
        'cpu_info': cpuinf.decode("UTF-8"),
        'operative_system': os.decode("UTF-8"),
        'version_os': ver_os.decode("UTF-8"),
        'process': process.decode("UTF-8")
    }
}

with open(nombreArchivo, 'w') as file:
    json.dump(monitoring, file, indent=6)

print (monitoring)


def monitoring_report(nombreArchivo):
    monitoring_report = {'users': sessions, 'cpuinfo': cpuinf,'operative_system': os, 'version_os': ver_os, 'process': process}
    resp = requests.post('192.168.1.11:8080/servers/monitoring', data=monitoring)
    