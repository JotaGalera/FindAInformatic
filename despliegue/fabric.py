from fabric.api import *

def Install():
  run('git clone https://github.com/JotaGalera/FindAInformatic')
  with cd("~/FindAInformatic/"):
    run('make')

def Start():
  with cd("~/FindAInformatic/"):
    run('gunicorn application:app')
    run('pgrep gunicorn > ~/id.tx') //Para asegurarnos que tenemos controlado cual es nuestro gunicorn

def Stop(): //Leemos el PID de nuestro gunicorn y lo matamos
  run(' var=$(head -1 ~/id.txt) ')
  run(' kill $var')

def RemoveAll():
  rm -r ~/*
