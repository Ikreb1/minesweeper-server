FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir Flask Flask-SQLAlchemy

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
