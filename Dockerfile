FROM python:3.12-slim
ENV TZ=UTC
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ src/
CMD ["python", "-m", "src.app"]
