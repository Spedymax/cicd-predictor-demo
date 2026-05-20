FROM ubuntu:22.04
WORKDIR /app
RUN apt-get update && apt-get install -y \
    python3.11 python3-pip build-essential \
    libpq-dev libssl-dev libffi-dev libxml2-dev libxslt1-dev \
    git curl wget vim htop tmux \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install --upgrade pip setuptools wheel
COPY requirements.txt requirements-dev.txt ./
RUN pip3 install -r requirements.txt -r requirements-dev.txt
COPY src/ src/
COPY tests/ tests/
COPY scripts/ scripts/
RUN python3 -m pytest tests/ --no-cov || true
RUN find / -name "*.pyc" -delete
EXPOSE 8080 9090
HEALTHCHECK --interval=30s CMD curl -f http://localhost:8080/health || exit 1
CMD ["python3", "-m", "src.app"]
