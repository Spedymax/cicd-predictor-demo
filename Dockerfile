FROM ubuntu:22.04
RUN apt-get update && apt-get install -y --no-install-recommends python3.11 python3-pip && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN python3.11 -m pip install -r requirements.txt
COPY src/ src/
CMD ["python3.11", "-m", "src.app"]
