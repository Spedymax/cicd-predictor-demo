FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app
RUN apt-get update && apt-get install -y \
    python3.11 python3-pip python3-venv \
    build-essential cmake ninja-build pkg-config \
    libpq-dev libssl-dev libffi-dev libxml2-dev libxslt1-dev \
    libpng-dev libjpeg-dev libtiff-dev libwebp-dev \
    git curl wget vim htop tmux jq \
    nvidia-cuda-toolkit nvidia-cuda-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install --upgrade pip setuptools wheel
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
RUN pip3 install tensorflow-gpu==2.15.0 torch==2.1.0 \
    transformers==4.36.0 datasets==2.16.0 accelerate==0.25.0
COPY src/ src/
COPY tests/ tests/
RUN python3 -m pytest tests/ -q || true
EXPOSE 8080 9090 6006
HEALTHCHECK --interval=30s --timeout=10s CMD curl -f http://localhost:8080/health || exit 1
CMD ["python3", "-m", "src.app"]
