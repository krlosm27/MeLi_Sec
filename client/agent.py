import subprocess
##import json
##from subprocess import PIPE, run
##import requests

def monitoring():
    prueba = subprocess.run(["ipconfig"])
    ##users = subprocess.run(["who"]) ## Usuarios Conectados
    ##cpuinf = subprocess.run(["lscpu"])  ## Informaciòn de CPU
    ##os = subprocess.run(["cat /etc/*release* | grep -E -i "^NAME="]) ## Sistema operativo
    ##ver_os = subprocess.run(["cat /etc/*release* | grep -E -i "^VERSION_ID"]) ## Versiòn del sistema operativo
    ##procss = subprocess.run(["ps -ef | sed 's/\\/\/\//g' | grep -v sed"]) ## Listado de procesos activos
    ##date = subprocess.run(["date"]) ## Fecha
    return prueba

print (monitoring())
print(type(monitoring())) ## conocer tipo de dato

##def monitoring_report(jsonresponse):

    ##monitoring_report = {'users': users, 'cpuinfo': cpuinf}
    ##resp = requests.post('192.168.1.11:8080/servers/monitoring', data=monitoring_report)
    ##monitoring_report = {"sessions":users}