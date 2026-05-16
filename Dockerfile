FROM ubuntu:99.04
RUN totally-fake-cmd --install everything
COPY nonexistent/ /app/
CMD ["python3.11", "-m", "src.app"]
