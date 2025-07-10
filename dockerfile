FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

# Ajustamos el CMD para apuntar a /app/core/manage.py
CMD ["sh", "-c", "python core/manage.py migrate && gunicorn core.wsgi:application --bind 0.0.0.0:8000"]