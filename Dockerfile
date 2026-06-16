FROM python:3.11-slim
LABEL org.opencontainers.image.title="cicd-predictor-demo"
LABEL org.opencontainers.image.source="https://github.com/Spedymax/cicd-predictor-demo"
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV APP_PORT=8080
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ src/
COPY tests/ tests/
RUN python -c "import src.app"
EXPOSE 8080
CMD ["python", "-m", "src.app"]
