FROM python:3.10-slim

# Mantenedor de la imagen
LABEL maintainer="Julian Salinas"

# Instalar dependencias del sistema necesarias para mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev gcc pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# Copiar el código del microservicio
COPY . /app

# Instalar dependencias de Python directamente (sin requirements.txt)
RUN pip install --no-cache-dir \
    Flask \
    Flask-Cors \
    Flask-SQLAlchemy \
    mysqlclient

# Exponer el puerto de la app
EXPOSE 5001

# Variable de entorno para Flask
ENV FLASK_APP=run.py

# Comando de inicio (modo desarrollo con flask run)
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]

