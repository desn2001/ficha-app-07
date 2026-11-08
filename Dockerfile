FROM python:3.14-slim

LABEL org.opencontainers.image.title="Ficha técnica APP-07 Rutas en Bici" \
      org.opencontainers.image.authors="desn2001, jufraa" \
      org.opencontainers.image.source="https://github.com/desn2001/ficha-app-07"

WORKDIR /app
COPY ficha_app.py .
CMD ["python", "ficha_app.py"]
