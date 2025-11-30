# Imagen base de Python
FROM python:3.11-slim

WORKDIR /app

# Copiar requirements si lo hay
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar la app
COPY . .

# Exponer puerto
EXPOSE 5000

# Comando para iniciar la app
CMD ["python", "app.py"]
