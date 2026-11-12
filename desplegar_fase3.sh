#!/bin/bash
echo "Creando carpeta de logs..."
mkdir -p logs
echo "Lanzando contenedor con persistencia y variables de entorno..."
docker run -d -p 5000:5000 --name monitor-persistente -v $(pwd)/logs:/app/logs -e APP_TITLE="Monitor de Mauri - Fase 3" monitor-app
echo "¡Fase 3 desplegada con éxito!"
