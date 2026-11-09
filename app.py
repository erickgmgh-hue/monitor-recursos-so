import os
import socket
import logging
from flask import Flask, render_template_string
import psutil
import time

app = Flask(__name__)

if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(filename='logs/app.log', level=logging.INFO)

@app.route('/')
def monitor():
    app_title = os.environ.get('APP_TITLE', 'Monitor Básico de Recursos')
    hostname = socket.gethostname()

    cpu_percent = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory()
    disco = psutil.disk_usage('/')
    
    ram_usada = round(memoria.used / (1024**3), 2)
    ram_disp = round(memoria.available / (1024**3), 2)
    disco_usado = round(disco.used / (1024**3), 2)
    disco_disp = round(disco.free / (1024**3), 2)
    cantidad_procesos = len(psutil.pids())
    uptime_segundos = int(time.time() - psutil.boot_time())

    return f"""
    <h1>{app_title}</h1>
    <p>Hostname: {hostname}</p>
    <p>CPU: {cpu_percent}%</p>
    <p>RAM Usada: {ram_usada} GB / Disponible: {ram_disp} GB</p>
    <p>Almacenamiento Usado: {disco_usado} GB / Disponible: {disco_disp} GB</p>
    <p>Cantidad de Procesos: {cantidad_procesos}</p>
    <p>Uptime: {uptime_segundos} segundos</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
