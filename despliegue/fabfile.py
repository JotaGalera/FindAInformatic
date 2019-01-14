from fabric.api import *

def Install():
  run('git clone https://github.com/JotaGalera/FindAInformatic')
  with cd("~/FindAInformatic/"):
    run('make')

def Start():
  with cd("~/FindAInformatic/"):
    run('sudo gunicorn --bind 0.0.0.0:80 application:app')
    run('pgrep gunicorn > ~/id.tx') #Para asegurarnos que tenemos controlado cual es nuestro gunicorn

def Stop(): #Leemos el PID de nuestro gunicorn y lo matamos
  run(' var=$(head -1 ~/id.txt) ')
  run(' sudo kill $var')

def RemoveAll():
  run(' rm -rf ~/* ')
