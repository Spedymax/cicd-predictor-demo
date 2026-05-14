FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3.11 python3-pip
WORKDIR /app
COPY requirements.txt .
RUN python3.11 -m pip install -r requirements.txt
COPY src/ src/
CMD ["python3.11", "-m", "src.app"]
