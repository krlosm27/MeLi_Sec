from subprocess import check_output
import json
import requests

sessions = check_output(["who"])
cpuinf = check_output(["lscpu"])
os = check_output(['cat /etc/*release* | grep -E -i PRETTY_NAME'], shell=True)
ver_os = check_output(['cat /etc/*release* | grep -E -i ^VERSION_ID'], shell=True)
process = check_output(['ps -ef | sed "s/u/o/g" | grep -v sed'], shell=True)
#process = check_output(["ps -ef | sed 's/\\/\/\//g' | grep -v sed"])
date = check_output(["date"])
ip_server = check_output(["ip addr show"])

monitoreo = [cpuinf, process, sessions, os, ver_os ] # lista de array de bits de los comandos ejecutados
nombreArchivo = ip_server.decode("UTF-8") + date.decode("UTF-8") + ".json" # concatenado de nombre de archivo json

with open(nombreArchivo, 'w') as archivoJson: # open (administra archivos) primer_arg = ruta_archivo segundo_arg = r - read, w-write
    for dato in monitoreo:
        datoDecodificado = dato.decode("UTF-8") # Decodifica cada array de bits en formato UTF-8 y lo guarda en nueva variable
        archivoJson.writelines(datoDecodificado)


 # res --> llevar a formato json
def monitoring_report(nombreArchivo):
    monitoring_report = {'users': sessions, 'cpuinfo': cpuinf,'operative_system': os, 'version_os': ver_os, 'process': process}
    resp = requests.post('192.168.1.11:8080/servers/monitoring', data=monitoring_report)
    