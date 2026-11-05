import os
import socket
import logging
from flask import Flask, render_template_string
import psutil

app = Flask(__name__)

# Configuración básica de logs (Para Sebas)
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(filename='logs/app.log', level=logging.INFO)

@app.route('/')
def monitor():
    # Variable de entorno con valor por defecto
    app_title = os.environ.get('APP_TITLE', 'Monitor Básico de Recursos')
    hostname = socket.gethostname()

    # Métricas del SO (Para Jade)
    cpu_percent = psutil.cpu_percent(interval=1)
    
    return f"<h1>{app_title}</h1><p>Hostname: {hostname}</p><p>CPU: {cpu_percent}%</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
