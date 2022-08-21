import subprocess
import jason
from subprocess import PIPE

users = run (Who) ## Usuarios Conectados
cpuinf = run (lscpu)  ## Informaciòn de CPU
os = run (cat /etc/*release* | grep -E -i) ## Sistema operativo
ver_os = run (cat /etc/ *release* | grep -E -i) ## Versiòn del sistema operativo
procss = run (ps -ef | sed 's/\\/\/\//g' | grep -v sed) ## Listado de procesos activos
date = run (date) ## Fecha
ip address = () ## ip del sevidor 
