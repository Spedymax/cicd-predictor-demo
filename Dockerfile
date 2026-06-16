FROM python:99.99-slim
LABEL org.opencontainers.image.title="cicd-predictor-demo-gpu"
ENV PYTHONUNBUFFERED=1 \
    CUDA_VISIBLE_DEVICES=0
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ src/
COPY tests/ tests/
ENABLE_GPU --all
EXPOSE 8080
CMD ["python", "-m", "src.app"]
